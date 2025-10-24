#from pyflink.table import EnvironmentSettings, TableEnvironment
from pyflink.table import EnvironmentSettings, TableEnvironment



import logging
import sys



def running_table():
    env_settings = EnvironmentSettings.in_streaming_mode()
    t_env = TableEnvironment.create(env_settings)
    
    
    # t_env.get_config().get_configuration().set_string("fs.s3a.access-key", "minioadmin")
    # t_env.get_config().get_configuration().set_string("fs.s3a.secret-key", "minioadmin")
    
    # t_env.get_config().get_configuration().set_string("state.checkpoints.dir", "local:///opt/flink/content/checkpoints")
    # t_env.get_config().get_configuration().set_string("state.savepoints.dir", "local:///opt/flink/content/savepoints")

    
    # t_env.get_config().get_configuration().set_string("fs.s3a.endpoint", "http://172.18.0.2:9000")
    # t_env.get_config().get_configuration().set_string("fs.s3a.path.style.access", "true")
    # t_env.get_config().get_configuration().set_string("fs.s3.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    

    t_env.execute_sql("""
    CREATE TABLE clientes (
        id INT,
        nome STRING,
        idade INT
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'simple-client-kafka-topic-input',
        'properties.bootstrap.servers' = 'wednesday-primary-cluster-kafka-bootstrap.kafka.svc:9092',
        'properties.group.id' = 'pyflink-consumer',
        'format' = 'json',
        'json.fail-on-missing-field' = 'false',
        'json.ignore-parse-errors' = 'true',
        'scan.startup.mode' = 'latest-offset' 
    )
    """)
    #'earliest-offset'
    
    t_env.execute_sql("""
        CREATE  TEMPORARY TABLE  kafka_output (
            client_id INT,
            client_name STRING,
            age INT
        ) WITH (
            'connector' = 'kafka',
            'topic' = 'simple-client-kafka-topic-output',
            'properties.bootstrap.servers' = 'wednesday-primary-cluster-kafka-bootstrap.kafka.svc:9092',
            'format' = 'json',
            'scan.startup.mode' = 'latest-offset'
        )
        """) 

    
    # t_env.execute_sql("""
    #     INSERT INTO kafka_output
    #     SELECT id AS client_id, nome AS name_client, idade  AS age FROM clientes
    #     """)
    

    t_env.execute_sql("""
        CREATE TABLE s3_sink (
            client_id INT,
            client_name STRING,
            age INT
        ) WITH (
            'connector' = 'filesystem',
            'path' = 'file:///opt/flink/content/output/simple-clientes',
            'format' = 'json'
        )
    """) 
    
    t_env.execute_sql("""
        CREATE TABLE s3_sink_18 (
            client_id INT,
            client_name STRING,
            age INT
        ) WITH (
            'connector' = 'filesystem',
            'path' = 'file:///opt/flink/content/output/simple-clientes-18',
            'format' = 'json'
        )
    """) 
    
    
    # t_env.execute_sql("""
    #     INSERT INTO s3_sink
    #     SELECT id AS client_id, nome AS name_client, idade  AS age FROM clientes
    #     """)   
    
    stmt_set = t_env.create_statement_set()

    stmt_set.add_insert("kafka_output", t_env.from_path("clientes"))
    stmt_set.add_insert("s3_sink", t_env.from_path("clientes"))
    stmt_set.add_insert("s3_sink_18",  t_env.sql_query("SELECT id, nome, idade FROM clientes WHERE idade > 18"))

    stmt_set.execute()
    
    # # Agora você pode fazer queries com Table API
    # t_env.execute_sql("""
    # SELECT count(1)
    # FROM clientes
    # """).print()
    
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
    running_table()