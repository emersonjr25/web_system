from flask import render_template, request
from app import app, db
from app.models.tables import Machine
from json import dumps
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import joblib

loaded_model = joblib.load('app/controllers/house_model.joblib')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('html/contact.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        values = [int(i) for i in request.form.to_dict().values()]
        values_database = [str(i) for i in request.form.to_dict().values()]
        values_to_model = np.array([values])
        prediction = loaded_model.predict(values_to_model)
        prediction_final = int(prediction)
        i = Machine(*values_database)
        db.session.add(i)
        db.session.commit()
        return render_template('html/result.html', prediction = prediction_final)

@app.route('/projects', methods=['GET'])
def project():
    return render_template('html/projects.html')

@app.route('/delete/<id>')
def delete(id):
    data = Machine.query.get(id)
    print(data)
    db.session.delete(data)
    db.session.commit()
    return render_template('index.html')

@app.route('/prediction', methods=['GET'])
def prediction():
    return render_template('html/prediction.html')

@app.route('/crud')
def crud():
    machine_learning = Machine.query.all()
    return render_template('html/crud.html', machine_learning=machine_learning)