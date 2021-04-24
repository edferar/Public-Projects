from pymongo import MongoClient


def insertDatabase(dados_insert):
    try:

        client = MongoClient('mongoDb', 27017)
        db = client.form_avc
        db.avc_proba.insert_one(dados_insert)


    except Exception as e:
        print(f"Falha ao inserir dados na base. Erro -> {e}")

    finally:
        print(f"Registrado com sucesso na base de dados")
