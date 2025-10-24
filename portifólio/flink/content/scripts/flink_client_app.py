#from pyflink.table import EnvironmentSettings, TableEnvironment
from pyflink.table import EnvironmentSettings, TableEnvironment
from pyflink.table import StreamTableEnvironment, DataTypes
from pyflink.datastream import StreamExecutionEnvironment, CheckpointingMode


import logging
import sys
import json
import re

def format_cols(schema: str):
    schema = schema.replace("\n", " ").strip()
    return flatten_fields(parse_fields(schema))

def parse_fields(s: str):
    fields = []
    i = 0
    while i < len(s):
        name_match = re.match(r"\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*", s[i:])
        if not name_match:
            break
        name = name_match.group(1)
        i += name_match.end()

        type_str, delta = extract_type(s[i:])
        fields.append((name, type_str.strip()))
        i += delta
        while i < len(s) and s[i] in ", ":
            i += 1
    return fields

def extract_type(s: str):
    s = s.strip()
    i = 0
    nested = 0
    while i < len(s):
        if s[i] == "<":
            nested += 1
        elif s[i] == ">":
            nested -= 1
        elif s[i] == "," and nested == 0:
            break
        i += 1
    return s[:i], i

def flatten_fields(fields, prefix=""):
    flat = []

    for name, dtype in fields:
        full_name = f"{prefix}.{name}" if prefix else name
        new_name = f"{prefix.replace('.','_').lower()}_{name.lower()}" if prefix else name.lower()
        base_type = dtype.split("<")[0].strip().upper()

        if base_type in ("ROW"):
            inner = re.search(r"<(.*)>", dtype, re.DOTALL)
            if not inner:
                flat.append(dict(full_name = full_name,new_name = new_name, dtype = dtype))
                continue
            inner_content = inner.group(1)
            

            if base_type == "ROW":
                inner_fields = parse_fields(inner_content)
                flat.extend(flatten_fields(inner_fields, full_name))
           
        else:
            flat.append(dict(full_name = full_name,new_name = new_name, dtype = dtype))
    return flat

# def format_cols_df(self, new_cols, schema, prefix=""):

#     for field in schema["fields"]:
#         chars_ = ["$", " ", "-", "[", "]", ".", "*", "'"]
#         field_name = field["name"].lower().lstrip(".")

#         if any(char in field["name"] for char in chars_):
#             field_name = (
#                 f"{prefix}['{field_name}']" if prefix else f"['{field_name}']"
#             )
#         else:
#             field_name = f"{prefix}.{field_name}" if prefix else field_name

#         new_name = field_name
#         for char in chars_:
#             new_name = new_name.replace(char, "_")

#         if "fields" in field["type"]:
#             self.format_cols_df(new_cols, field["type"], field_name)
#         else:
#             new_cols.append(f"{field_name} AS {new_name}")


def running_table():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.enable_checkpointing(60000)  # a cada 60 segundos
    checkpoint_config = env.get_checkpoint_config()
    env.get_checkpoint_config().set_checkpointing_mode(CheckpointingMode.EXACTLY_ONCE)
    env.get_checkpoint_config().set_checkpoint_timeout(6000)
    env.get_checkpoint_config().set_max_concurrent_checkpoints(1)


    settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    t_env = StreamTableEnvironment.create(env, environment_settings=settings)
    t_env.get_config().get_configuration().set_string(
        "state.checkpoints.dir",
        "file:///opt/flink/content/checkpoints/clientes-bronze"
    )
    t_env.get_config().get_configuration().set_string(
        "state.backend", "rocksdb"
    )
    
    
    table_name = "{layer}_clientes"
    input_topic = 'client-kafka-{layer}-topic'
    output_topic = 'client-kafka-{layer}-topic'
    landing_input_schema = """
                eventDate TIMESTAMP(3),
                requestId STRING,
                Data ROW<
                    id INT,
                    nome STRING,
                    endereco ROW<
                    rua STRING,
                    numero STRING,
                    cidade STRING,
                    estado STRING,
                    localizacao ROW<
                        latitude DOUBLE,
                        longitude DOUBLE
                    >
                    >,
                    telefones ARRAY<ROW<
                    tipo STRING,
                    numero STRING
                    >>,
                    comprasRecentes ARRAY<ROW<
                    produto STRING,
                    preco DOUBLE,
                    caracteristicas MAP<STRING, STRING>
                    >>
                >
    """
    stmt_set = t_env.create_statement_set()
    
    ##################Bronze#######################
    t_env.execute_sql(f"""
    CREATE TEMPORARY TABLE {table_name.format(layer='bronze')} ({landing_input_schema}) WITH (
        'connector' = 'kafka',
        'topic' = '{input_topic.format(layer='landing')}',
        'properties.bootstrap.servers' = 'wednesday-primary-cluster-kafka-bootstrap.kafka.svc:9092',
        'properties.group.id' = 'pyflink-consumer-bronze',
        'format' = 'json',
        'json.fail-on-missing-field' = 'false',
        'json.ignore-parse-errors' = 'true',
        'scan.startup.mode' = 'group-offsets' ,
        'sink.semantic' ='exactly-once'

    )
    """)
    
    
    flattened = format_cols(landing_input_schema)
    bronze_output_schema = str([f'{i["new_name"]} { i["dtype"]}' for i in flattened]).strip("[]").replace("'", "")
    new_cols = [f'{i["full_name"]} AS {i["new_name"]}' for i in flattened]
    
    query = f"SELECT {','.join(list(filter(None, new_cols)))} FROM {table_name.format(layer='bronze')}"
        
    # #'earliest-offset'
    
    
    t_env.execute_sql(f"""
        CREATE TEMPORARY TABLE  kafka_output_bronze ({bronze_output_schema}) WITH (
            'connector' = 'kafka',
            'topic' = '{output_topic.format(layer='bronze')}',
            'properties.bootstrap.servers' = 'wednesday-primary-cluster-kafka-bootstrap.kafka.svc:9092',
            'format' = 'json',
            'scan.startup.mode' = 'earliest-offset'

        )
        """) 
        
    t_env.execute_sql(f"""
        CREATE TABLE s3_sink_bronze ({bronze_output_schema}
        ) WITH (
            'connector' = 'filesystem',
            'path' = 'file:///opt/flink/content/output/{table_name.format(layer='bronze')}',
            'format' = 'json'
        )
    """) 
    
    
    

    stmt_set.add_insert("s3_sink_bronze", t_env.sql_query(query))
    stmt_set.add_insert("kafka_output_bronze", t_env.sql_query(query))
    
    ###########Silver#######################
    t_env.execute_sql(f"""
    CREATE TEMPORARY TABLE {table_name.format(layer='silver')} ({bronze_output_schema}) WITH (
        'connector' = 'kafka',
        'topic' = '{input_topic.format(layer='bronze')}',
        'properties.bootstrap.servers' = 'wednesday-primary-cluster-kafka-bootstrap.kafka.svc:9092',
        'properties.group.id' = 'pyflink-consumer-silver',
        'format' = 'json',
        'json.fail-on-missing-field' = 'false',
        'json.ignore-parse-errors' = 'true',
        'scan.startup.mode' = 'group-offsets' ,
        'sink.semantic' ='exactly-once'

    )
    """)

    table_api_telefone = t_env.sql_query(f"""  
        SELECT
            eventdate,
            requestid,
            data_id AS id,
            tipo,
            numero
        FROM {table_name.format(layer='silver')} 
        CROSS JOIN UNNEST(data_telefones) AS tel(tipo, numero)
        
        """)
        #LATERAL TABLE()
    t_env.create_temporary_view("table_api_telefone", table_api_telefone)
    
    silver_output_schema = table_api_telefone.get_schema()
    print("silver_output_schema ", silver_output_schema)
    silver_output_schema = str([f"{name} {dtype}" for name, dtype in zip(silver_output_schema.get_field_names(), silver_output_schema.get_field_data_types())]).strip("[]").replace("'", "")
    print("silver_output_schema ", silver_output_schema)
    
    
    
    
    t_env.execute_sql(f"""
        CREATE TEMPORARY TABLE  kafka_output_silver ({silver_output_schema}) WITH (
            'connector' = 'kafka',
            'topic' = '{output_topic.format(layer='silver')}',
            'properties.bootstrap.servers' = 'wednesday-primary-cluster-kafka-bootstrap.kafka.svc:9092',
            'format' = 'json',
            'scan.startup.mode' = 'earliest-offset'

        )
        """) 
    t_env.execute_sql(f"""
        CREATE TABLE s3_sink_silver ({silver_output_schema}
        ) WITH (
            'connector' = 'filesystem',
            'path' = 'file:///opt/flink/content/output/{table_name.format(layer='silver')}/telefones',
            'format' = 'json'
        )
    """) 
    
    stmt_set.add_insert("s3_sink_silver", t_env.from_path("table_api_telefone"))
    stmt_set.add_insert("kafka_output_silver", t_env.from_path("table_api_telefone"))
    
    stmt_set.execute()
    

    
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
    running_table()