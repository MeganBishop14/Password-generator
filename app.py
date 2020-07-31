# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_password
from datetime import datetime
from model import checkReq


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template ('index.html')
@app.route('/results', methods= ['GET', 'POST'])
def results():
    print(request.form)
    password_length = request.form["length"]
    password_capital = checkReq(request.form, "capitalization")
    password_special = checkReq(request.form, "special")
    password_numbers = checkReq(request.form, "digits")
    print(password_numbers)
    password = get_password(password_length, password_numbers, password_capital, password_special)
    return render_template('results.html', password_length=password_length, password_numbers=password_numbers, password_capital=password_capital, password_special=password_special, password=password, time=datetime.now())







