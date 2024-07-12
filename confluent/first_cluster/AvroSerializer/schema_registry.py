from message import Message
from confluent_kafka.schema_registry import SchemaRegistryClient

class SchemaRClient():
    def __init__(self,url,user_api_auth,pw_api_auth):
        self.url = url
        self.client = self.generate_client(user_api_auth,pw_api_auth)

    def generate_client(self,user_api_auth,pw_api_auth):
        return SchemaRegistryClient({'url':self.url,
                            'basic.auth.user.info': f"{user_api_auth}:{pw_api_auth}"
                            })
    
    def get_schema_str(self,schema_id):
        return self.client.get_schema(schema_id).schema_str

            
