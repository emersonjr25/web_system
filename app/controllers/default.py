from flask import render_template
from app import app

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('html/contact.html')

@app.route('/projects', methods=['GET'])
def project():
    return render_template('html/projects.html')

@app.route('/prediction', methods=['GET'])
def prediction():
    return render_template('html/prediction.html')