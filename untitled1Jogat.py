# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:36:35 2020

@author: s613116
"""

from flask import Flask, render_template,request
import json

app = Flask(__name__)



@app.route('/')
def home():
    with open('templates/JogatinDate.txt', 'r') as f:
        date = f.read()
    return render_template('untitled3Jogat.html',JogatDate = date)


@app.route('/postdate', methods=['POST'])
def postdate():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    #result = json.loads(output) #this converts the json output to a python dictionary
    # print(result) # Printing the new dictionary
    with open('templates/JogatinDate.txt', 'w') as f:
        f.write(output)
    return output 

if __name__ == '__main__':
	app.run()