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

if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)