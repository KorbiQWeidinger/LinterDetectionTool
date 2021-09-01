import json
import os
import re

from src.constants import file_regex_whitelist
from src.constants.linters import codeql, checkstyle, codacy, coverity, findbugs, spotbugs, pmd, sonarqube, \
    blacklist

linters = {codeql, checkstyle, codacy, coverity, findbugs, spotbugs, pmd, sonarqube, blacklist}


class LinterFinding(object):

    def __init__(self, linter_name, path, signal, line=-1):
        self.linter_name = linter_name
        self.path = path
        self.signal = signal
        self.line = line

    def write(self, full_name):
        url = "https://github.com/" + full_name + "/blob/master" + self.path.replace("\\", "/")
        line_string = ""
        if self.line >= 0:
            line_string = f" in line {self.line}"
        return self.signal + line_string + " in " + url + line_string

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


def is_file_of_interest(file):
    for regex in file_regex_whitelist.file_whitelist:
        if bool(re.search(regex, file)):
            return True
    return False


def find_signals(search_path):
    result = []
    for root, directory, files in os.walk(search_path):
        result.extend(find_signals_in_files(files, root, search_path))
        result.extend(find_signals_in_filenames(files, root, search_path))
        result.extend(find_signals_in_filenames(directory, root, search_path))
    return result


def find_signals_in_files(files, root, search_path):
    result = []
    for fn in files:
        if not is_file_of_interest(fn):
            continue
        opened_file = open(root + "/" + fn, "r", encoding='utf8')
        try:
            line_number = -1
            for line in opened_file.readlines():
                line_number += 1
                for linter in linters:
                    for signal_word in linter.signal_words:
                        if bool(re.search(signal_word, line)):
                            result.append(
                                LinterFinding(path=root.replace(search_path, "") + "/" + fn,
                                              signal=signal_word, line=line_number, linter_name=linter.NAME))
        except UnicodeDecodeError:
            continue
        opened_file.close()
    return result


def find_signals_in_filenames(keywords, root, search_path):
    result = []
    for key in keywords:
        for linter in linters:
            for rx in linter.file_regex:
                if bool(re.search(rx, key)):
                    result.append(LinterFinding(path=root.replace(search_path, "") + "/" + key,
                                                signal=rx, linter_name=linter.NAME))
    return result


def save_findings_to_files(full_name, project_path, result_path):
    signal_findings = find_signals(project_path)

    url = "https://github.com/" + full_name

    if len(signal_findings) == 0:
        no_findings_file = open(result_path + "/no_findings.txt", "a")
        no_findings_file.write(url + "\n")
        no_findings_file.close()
        return

    for linter in linters:
        findings = []
        for signal_finding in signal_findings:
            if signal_finding.linter_name == linter.NAME:
                findings.append(signal_finding)
        if len(findings) > 0:
            new_file = open(
                result_path + "/" + full_name.replace("/", "_") + "+" + linter.NAME + "+" + len(
                    findings).__str__() + ".txt", "w+")
            for finding in findings:
                new_file.write(finding.write(full_name))
            new_file.close()
