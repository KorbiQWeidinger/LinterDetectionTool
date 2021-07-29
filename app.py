# app.py
import os
import sys
import json
from src.linter_analysis import find_signals

from flask import Flask, render_template, jsonify

app = Flask(__name__)  # name for the Flask app (refer to output)
# running the server
app.run(debug=True)  # to allow for debugging and auto-reload

app = Flask(__name__)

TMP = os.getcwd() + '\\tmp'


def clone_project(full_name):
    print("############# Cloning Project ################", file=sys.stdout)
    os.system(f"git clone https://github.com/{full_name}.git " + TMP + "/" + full_name.split("/")[1])
    print("############# Cloning Complete ###############", file=sys.stdout)


def clear_and_create_tmp():
    os.system('rmdir "%s" /s /q' % TMP)
    os.system('mkdir tmp')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/trigger-analysis/<owner>/<name>")
def trigger_analysis(owner, name):
    clear_and_create_tmp()
    full_name = f"{owner}/{name}"
    clone_project(full_name)
    signals = find_signals(f"{TMP}/{name}")
    return render_template('signals.html', signals=signals, full_name=full_name)
