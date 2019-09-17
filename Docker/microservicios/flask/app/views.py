from flask import render_template, request
from app import app
import os

@app.route("/")
def index():
    return render_template('app.html')

@app.route('/resp', methods=['POST'])
def resp():
    if request.method == 'POST':
		num1 = request.form['n1']
		num2 = request.form['n2']
		oper = request.form['operacion']