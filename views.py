from flask import Blueprint, render_template, request, jsonify, redirect, url_for


views = Blueprint(__name__, "views")

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
    #llamado a la funcion con los pacientes cercanos
    return render_template('index.html', age = age, sex = sex, ethnicity = ethnicity,mentalHealth = mentalHealth,generalHealth = generalHealth,cancerType = cancerType, cancerStage = cancerStage)


@views.route("/json")
def get_json():
    return jsonify({"name": "Tim", "coolness": 10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)