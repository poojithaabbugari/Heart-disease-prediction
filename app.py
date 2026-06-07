import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

import warnings
warnings.filterwarnings('ignore')



app = Flask(__name__)




@app.route("/about")
def about1():
    return render_template("about.html")


@app.route('/')
@app.route('/home1')
def home1():
	return render_template('home1.html')


@app.route('/home2')
def home2():
	return render_template('home2.html')


@app.route('/predict',methods=['POST'])
def predict():
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final4=[np.array(int_features)]
    model = joblib.load('model1.sav')
    predict = model.predict(final4)

    if predict == 0:
        output = "NEGATIVE, PATIENT IS NOT SUFFER FROM HEART DISEASE!" 
    elif predict == 1:
        output = "POSITIVE, PATIENT IS SUFFER FROM HEART DISEASE!"  
    
    
    return render_template('prediction.html', output=output)


@app.route('/predict1',methods=['POST'])
def predict1():
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final4=[np.array(int_features)]
    model = joblib.load('model2.sav')
    predict = model.predict(final4)

    if predict == 0:
        output = "NEGATIVE, PATIENT IS NOT SUFFER FROM HEART DISEASE!" 
    elif predict == 1:
        output = "POSITIVE, PATIENT IS SUFFER FROM HEART DISEASE!"  
    
    
    return render_template('prediction.html', output=output)



if __name__ == "__main__":
    app.run(debug=True)
