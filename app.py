# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 00:18:12 2022

@author: 91931
"""

import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)
model = pickle.load(open('Project3_KNN.pkl','rb')) 


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    exp1 = float(request.args.get('exp1'))
    exp2 = float(request.args.get('exp2'))
    exp3 = float(request.args.get('exp3'))
    exp4 = float(request.args.get('exp4'))
    exp5 = float(request.args.get('exp5'))
    exp6 = float(request.args.get('exp6'))
    
    prediction = model.predict([[exp1,exp2,exp3,exp4,exp5,exp6]])
    
    if prediction==[1]:
      prediction = "Survived"
    else:
      prediction = "Rest In Peace"  
    print(prediction)  
        
    return render_template('index.html', prediction_text='Titanic Survivor Analysis Model  has predicted Whether Passenger Survived or Not : {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug = True)