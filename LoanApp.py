# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:54:15 2019

@author: sagar
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('loan_index.html')

@app.route('/predict', methods = ['Post'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    return render_template('loan_index.html', prediction_text='Employee is Pakka {}'.format(final_features))
    
    

if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)
    print(final_features)