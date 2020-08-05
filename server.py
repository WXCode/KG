#!/usr/bin/env python
# coding: utf-8

from flask import Flask, redirect, url_for, request,send_file
from flask import render_template
import keyword_graph
from flask import jsonify
import pandas as pd
import json
app = Flask(__name__, template_folder="./templates")

app.config['TEMPLATES_AUTO_RELOAD'] = True
wrd_vecs = ''  

@app.route('/success/<name>') 
def success(name):
    if request.method == 'POST':
        user = request.form['nm'] 
        return redirect(url_for('success',name = user,_external=True)) 
    keyword_graph.keywords(name)
 
    return render_template('kg.html')



@app.route('/wrdvecs') 
def wrdvecs():   
    with open('test.json','r') as f:
        wrd_vecs = json.load(f)
    return jsonify(wrd_vecs)



@app.route('/',methods = ['POST', 'GET']) 
def login(): 
    if request.method == 'POST':       
        user = request.form['nm'] 
        return redirect(url_for('success',name = user,_external=True)) 
    else:
        return render_template('index.html')

if __name__ == '__main__': 
    app.run(host = "0.0.0.0",port = 5000) 


# In[ ]:




