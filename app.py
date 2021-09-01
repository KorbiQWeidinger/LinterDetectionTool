# app.py
import os
import sys

from git_analysis import clone_project
from src.linter_analysis import find_signals, linters

import flask
from flask import Flask, render_template, url_for

from util import clear_and_create, get_findings_for_linter

app = Flask(__name__)  # name for the Flask app (refer to output)
# running the server

# port = int(os.getenv('PORT'))

# print(port, file=sys.stdout)
# print(flask.__version__)

TMP = os.getcwd() + '/tmp'


def back_scape(st):
    return st.replace("\\", "/")


@app.route("/")
def home():
    return render_template('index.html', url_for=url_for)


@app.route("/trigger-analysis/<owner>/<name>")
def trigger_analysis(owner, name):
    clear_and_create(TMP)
    full_name = f"{owner}/{name}"
    clone_project(full_name, TMP)
    findings = find_signals(f"{TMP}/{name}")

    return render_template('findings.html', findings=findings, full_name=full_name, linters=linters,
                           get_findings_for_linter=get_findings_for_linter, len=len, back_scape=back_scape)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # , port=port)
