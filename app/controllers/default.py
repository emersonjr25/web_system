from flask import render_template, request
from app import app, db
from app.models.form import MachineTwo
from app.models.tables import Machine
from json import dumps

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('html/contact.html')

@app.route('/result', methods=['POST'])
def result():
   # if request.method == 'POST':
  #      return dumps(request.form)
 # model4.predict(np.array([X_test.iloc[0, :]]))
#a = np.array([X_test.iloc[0, :]])
#X_test.info
    return render_template('html/result.html')

@app.route('/projects', methods=['GET'])
def project():
    return render_template('html/projects.html')

@app.route('/prediction', methods=['GET'])
def prediction():
    return render_template('html/prediction.html')