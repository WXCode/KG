#!/usr/bin/env python
# coding: utf-8

from flask import Flask, redirect, url_for, request,send_file
from flask import render_template
import keyword_graph

app = Flask(__name__, template_folder="./templates")
  
#app.config['SERVER_NAME'] = '0.0.0.0:5000'
@app.route('/success/<name>') 
def success(name):
    print("Redirect",name)
    keyword_graph.keywords(name)
    return send_file('templates/Knowledge_Graph.svg')
    #return keyword_graph.keyword("%s" %name)

    

@app.route('/',methods = ['POST', 'GET']) 
def login(): 
    if request.method == 'POST':       
        user = request.form['nm'] 
        return redirect(url_for('success',name = user,_external=True)) 
    else:
        return render_template('nm.html')

if __name__ == '__main__': 
    app.run(host = "0.0.0.0",port = 5000) 


# In[ ]:




