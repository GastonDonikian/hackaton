from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from src.cancerPCA import *
import json
views = Blueprint(__name__, "views")


import json

column_names = ["cancerType","patientID","age","sex","ethnicity",
                    "mentalHealth","generalHealth","tumorSize","cancerStage",
                    "surgicalMethod","radiationMethod","chemotherapy",
                    "effectivenessOfTreatment","descripcion","similarity"]
cancerTypes = ['Adenocarcinoma','Carcinosarcoma']
sexes = ['Male', 'Female']
ethnicities = ['Caucasian','African American','Other']


def numpy_to_json(arr):
    
    # Convert numpy array to list of dictionaries
    data = [dict(zip(column_names, row)) for row in arr]
    #Convert to JSON string
    #iterate in date and change types to string to string
    for i in range(len(data)):
        data[i]['cancerType'] = cancerTypes[data[i]['cancerType']]
        data[i]['sex'] = sexes[data[i]['sex']]
        data[i]['ethnicity'] = ethnicities[data[i]['ethnicity']]
    print('este que esta aca')
    json_string = json.dumps(data)
    return data

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/", methods=["POST"])
def getValue():
    age = request.form.get("age")
    sex = request.form.get("sex")
    ethnicity = request.form.get("ethnicity")
    mentalHealth = request.form.get("mentalHealth")
    generalHealth = request.form.get("generalHealth")
    cancerType = request.form.get("cancerType")
    cancerStage = request.form.get("cancerStage")
    tumorSize = request.form.get("tumorSize")
    #llamado a la funcion con los pacientes cercanos

    # Example usage of the function
    input_point = {'age':int(age), 'sex':int(sex),'ethnicity':int(ethnicity),'mentalHealth':int(mentalHealth),'generalHealth':int(generalHealth),'tumorSize':float(tumorSize),'cancerType':int(cancerType),'cancerStage':int(cancerStage)}
    #input_point = {'age':70, 'sex':0,'ethnicity':1,'mentalHealth':4,'generalHealth':10,'tumorSize':10,'cancerType':0,'cancerStage':1}
    answer = get_nearest_points(input_point)
    input_point['cancerType'] = cancerTypes[input_point['cancerType']]
    input_point['sex'] = sexes[input_point['sex']]
    input_point['ethnicity'] = ethnicities[input_point['ethnicity']]
    #ponele que answer es json con cada caso + porcentaje de similaridad
    return render_template('answer.html',data=numpy_to_json(answer), columnNames = column_names, patient=input_point)


@views.route("/json")
def get_json():
    return jsonify({"name": "Tim", "coolness": 10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)