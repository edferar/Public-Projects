
from flask import Flask, request, jsonify
from flask_cors import CORS
from get_predicao import get_predict_proba
import json
from gevent.pywsgi import WSGIServer
from database_mongo import insertDatabase
import datetime
#import joblib


app = Flask("dockerRoutes")
CORS(app)#, resources={"dockerRoutes": {"origins": "*"}})

#model = joblib.load('../../modelo/model.pkl')

@app.route("/get_teste",methods=['GET'])
def get_teste():
    return(getResponse(200,"Registro realizado com sucesso!","return_pred",54.0))

@app.route("/get_predicao_modelo",methods=['POST'])
def get_predicao_app():
    #body = request.args.to_dict()
    body = request.get_json()
    
    if ("gender" not in body):
        return getResponse(400, "O parametro gender é obrigatório!")

    if ("age" not in body):
        return getResponse(400, "O parametro age é obrigatório!")

    if ("hypertension" not in body):
        return getResponse(400, "O parametro hypertension é obrigatório!")
        
    if ("heart_disease" not in body):
        return getResponse(400, "O parametro heart_disease é obrigatório!")

    if ("ever_married" not in body):
        return getResponse(400, "O parametro ever_married é obrigatório!")
        
    if ("Residence_type" not in body):
        return getResponse(400, "O parametro Residence_type é obrigatório!")

    if ("avg_glucose_level" not in body):
        return getResponse(400, "O parametro avg_glucose_level é obrigatório!")
    
    if ("bmi" not in body):
        return getResponse(400, "O parametro bmi é obrigatório!")
    
    if ("smoking_status" not in body):
        return getResponse(400, "O parametro smoking_status é obrigatório!")

    params = [[body["gender"] , body["age"] , body["hypertension"] , 
        body["heart_disease"] , body["ever_married"] , body["work_type"] , 
        body["Residence_type"] , body["avg_glucose_level"] , body["bmi"] , 
        body["smoking_status"]]]

    score = get_predict_proba(params)

    body.update({"data_solicitacao":datetime.datetime.utcnow()})
    print(body)
    insertDatabase(body)

    response = getResponse(200,"Registro realizado com sucesso!","return_pred",score)
    print(response)

    return response


def getResponse(status, mensagem, ncont = False, cont = False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if (ncont and cont):
        response[ncont] = cont
        

    return response

if __name__ == "__main__":
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
    #app.run()
