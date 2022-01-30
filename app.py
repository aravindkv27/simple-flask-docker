import imp
from flask import Flask, render_template, request
import json

app=Flask(__name__)

@app.route('/')
def start():
    name={
        'First name':'Aravind',
        'Second name':'K V'
    }

    return name

if __name__=='__main__':

    app.run(debug=True)