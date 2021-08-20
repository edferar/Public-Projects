import boto3
import pandas as pd 

#cliente aws s3

s3_cliente = boto3.client('s3')

s3_cliente.download_file('datalake-edneyferreira-edc',
    'data/username-password-recovery-code.csv',
    'data_local/username-password-recovery-code.csv')

s3_cliente.upload_file('data_local/username.csv',
    'datalake-edneyferreira-edc','data/username.csv')
df = pd.read_csv('data_local/username-password-recovery-code.csv',sep=';')

print(df)