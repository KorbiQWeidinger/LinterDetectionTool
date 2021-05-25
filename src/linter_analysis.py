import os
import re

from src.linter.constants import blacklist, checkstyle, conqat, findbugs, infer, moose, pmd, pvs_studio, semgrep, \
    semmle, sonarqube, spotbugs

linters = {blacklist, checkstyle, conqat, findbugs, infer, moose, pmd, pvs_studio, semgrep, semmle, sonarqube, spotbugs}

SAVE_TO_PATH = """I:\\BachelorThesis\\AnalysedProjects\\ManualAnalysis"""


class LinterFinding(object):

    def __init__(self, project_id, linter_name, path, signal, line=-1):
        self.linter_name = linter_name
        self.project_id = project_id
        self.path = path
        self.signal = signal
        self.line = line

    def write(self, full_name):
        url = "https://github.com/" + full_name + "/blob/master" + self.path.replace("\\", "/")
        line_string = ""
        finding_type = "File/Folder Finding"
        if self.line >= 0:
            line_string = " in line " + self.line.__str__()
            finding_type = "Word in File Finding"
        return finding_type + ": " + self.signal + line_string + " in " + url + "\n"


def find_signal_words(search_path):
    result = []
    for root, directory, files in os.walk(search_path):
        for fn in files:
            opened_file = open(root + "\\" + fn, "r", encoding='utf8')
            try:
                line_number = -1
                for line in opened_file.readlines():
                    line_number += 1
                    for linter in linters:
                        for signal_word in linter.signal_words:
                            if bool(re.search(signal_word, line)):
                                result.append(
                                    LinterFinding(project_id=0, path=root.replace(search_path, "") + "\\" + fn,
                                                  signal=signal_word, line=line_number, linter_name=linter.NAME))
            except UnicodeDecodeError:
                continue
            opened_file.close()
    return result


def find_files_and_folders(search_path):
    result = []
    for root, directory, files in os.walk(search_path):
        for fn in files:
            for linter in linters:
                for rx in linter.file_regex:
                    if bool(re.search(rx, fn)):
                        result.append(LinterFinding(project_id=0, path=root.replace(search_path, "") + "\\" + fn,
                                                    signal=rx, linter_name=linter.NAME))
        for dr in directory:
            for linter in linters:
                for rx in linter.file_regex:
                    if bool(re.search(rx, dr)):
                        result.append(LinterFinding(project_id=0, path=root.replace(search_path, "") + "\\" + dr,
                                                    signal=rx, linter_name=linter.NAME))
    return result


def save_findings_to_db():
    # TODO
    return


def save_findings_to_files(full_name, project_path, result_path):

    signal_file_findings = find_files_and_folders(project_path)
    signal_word_findings = find_signal_words(project_path)

    url = "https://github.com/" + full_name

    if (len(signal_word_findings) + len(signal_file_findings)) == 0:
        no_findings_file = open(result_path + "\\no_findings.txt", "a")
        no_findings_file.write(url + "\n")
        no_findings_file.close()
        return

    for linter in linters:
        findings = []
        for signal_file_finding in signal_file_findings:
            if signal_file_finding.linter_name == linter.NAME:
                findings.append(signal_file_finding)
        for signal_word_finding in signal_word_findings:
            if signal_word_finding.linter_name == linter.NAME:
                findings.append(signal_word_finding)
        if len(findings) > 0:
            new_file = open(result_path + "\\" + full_name.replace("/", "_") + "+" + linter.NAME + "+" + len(findings).__str__() + ".txt", "w+")
            for finding in findings:
                new_file.write(finding.write(full_name))
            new_file.close()
