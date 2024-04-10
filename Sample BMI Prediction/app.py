from flask import Flask, render_template, redirect, url_for, request
import pickle

app = Flask(__name__)

fileObj = open('model.obj', 'rb')
model = pickle.load(fileObj)

@app.route("/")
def index():
    return render_template('app.html')

@app.route("/predict",methods = ['POST', 'GET'])
def predict(bmi=None):
    if request.method == "POST":
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        gender = request.form.get('gender')
        if(gender==None):
            gender = 0;
        else:
            gender = int(request.form.get('gender'))
        bmi = model.predict([[height, weight, gender]])
        if(bmi == 0):
            bmi = "Extremely Weak"
        elif(bmi == 1):
            bmi = "Weak"
        elif(bmi == 2):
            bmi = "Normal"
        elif(bmi == 3):
            bmi = "Overweight"
        elif(bmi == 4):
            bmi = "Obesity"
        elif(bmi == 5):
            bmi = "Extreme Obesity"
        else:
            return render_template('app.html')
        return render_template('app.html', bmi=bmi)
    return render_template('app.html')
