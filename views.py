from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from src.cancerPCA import *
import json
views = Blueprint(__name__, "views")


import json

column_names = ["cancerType","patientID","age","sex","ethnicity",
                    "mentalHealth","generalHealth","tumorSize","cancerStage",
                    "surgicalMethod","radiationMethod","chemotherapy",
                    "effectivenessOfTreatment","descripcion"]

def numpy_to_json(arr):
    
    # Convert numpy array to list of dictionaries
    data = [dict(zip(column_names, row)) for row in arr]
    # Convert to JSON string
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
    #ponele que answer es json con cada caso + porcentaje de similaridad
    return render_template('answer.html',data=numpy_to_json(answer), columnNames = column_names)


@views.route("/json")
def get_json():
    return jsonify({"name": "Tim", "coolness": 10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)