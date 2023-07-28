from flask import render_template
from app import app, db
from app.models.form import MachineTwo
from app.models.tables import Machine

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('html/contact.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    form = MachineTwo()
    print(form.Lot_size.data)
    return render_template('html/result.html')

@app.route('/projects', methods=['GET'])
def project():
    return render_template('html/projects.html')

@app.route('/prediction', methods=['GET'])
def prediction():
    return render_template('html/prediction.html')