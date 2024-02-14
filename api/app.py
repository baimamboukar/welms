"""WELMS API BACKEND"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def abcrf():
    """--Returns index.html--"""

    return render_template('index.html')


@app.route('/members')
def members():
    """--Returns Memebexrs--"""
    return render_template('team.html')
