def GetProducerConfig():
    return {
    # User-specific properties that you must set
    'bootstrap.servers': 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
    'sasl.username':     '',
    'sasl.password':     '',
    # Fixed properties
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms':   'PLAIN',
    'acks':              'all'
}

def GetConsumerConfig():
    return {
        # User-specific properties that you must set
        'bootstrap.servers': 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
        'sasl.username':     '',
        'sasl.password':     '',
        #'schema.registry.url' : 'http://pkc-12576z.us-west2.gcp.confluent.cloud:8081',
        # Fixed properties
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms':   'PLAIN',
        'group.id':          'kafka-python-getting-started',
        'auto.offset.reset': 'earliest'
    }