import pickle
import pandas as pd
import numpy as np

def load_model():
    try:
        model = pickle.load(open('../../modelo/model.sav','rb'))
    except Exception as e:
        print(f"Falha ao realizar leitura do modelo. Erro -> {e}")
    finally:
        return model

def get_predict_proba(params_list):
    try:
        model = load_model()
        proba = model.predict_proba(params_list)
        proba = round(proba[0][1] * 100)
    except Exception as e:
        print(f"Falha ao gerar score. Erro -> {e}")
    finally:
        return  proba


def get_predict(params_list):
    try:
        model = load_model()
        pred = model.predict(params_list)
    except Exception as e:
        print(f"Falha ao gerar predição. Erro -> {e}")
    finally:
        return pred[0]
    
    



