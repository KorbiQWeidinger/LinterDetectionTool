# app.py
import os
import sys
import json
from src.linter_analysis import find_signals, linters

import flask
from flask import Flask, render_template, url_for

app = Flask(__name__)  # name for the Flask app (refer to output)
# running the server
app.run(debug=False, host='0.0.0.0')  # to allow for debugging and auto-reload

app = Flask(__name__)

TMP = os.getcwd() + '\\tmp'

print(flask.__version__)


def clone_project(full_name):
    print("############# Cloning Project ################", file=sys.stdout)
    os.system(f"git clone https://github.com/{full_name}.git " + TMP + "/" + full_name.split("/")[1])
    print("############# Cloning Complete ###############", file=sys.stdout)


def clear_and_create_tmp():
    os.system('rmdir "%s" /s /q' % TMP)
    os.system('mkdir tmp')


def get_findings_for_linter(linter_name, findings, file_findings=False):
    result = []
    for finding in findings:
        if finding.linter_name == linter_name:
            if finding.line == -1 and file_findings:
                result.append(finding)
            if finding.line != -1 and not file_findings:
                result.append(finding)
    return result


def back_scape(st):
    return st.replace("\\", "/")


@app.route("/")
def home():
    return render_template('index.html', url_for=url_for)


@app.route("/trigger-analysis/<owner>/<name>")
def trigger_analysis(owner, name):
    clear_and_create_tmp()
    full_name = f"{owner}/{name}"
    clone_project(full_name)
    findings = find_signals(f"{TMP}/{name}")

    return render_template('findings.html', findings=findings, full_name=full_name, linters=linters,
                           get_findings_for_linter=get_findings_for_linter, len=len, back_scape=back_scape)
