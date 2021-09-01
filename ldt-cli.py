import os
import sys

from git_analysis import clone_project
from linter_analysis import find_signals, linters
from util import get_findings_for_linter

TMP = os.getcwd() + '/tmp'


def clear_tmp():
    os.system('rm -rf tmp')


def evaluate_github_repo(owner, name):
    clone_project(f"{owner}/{name}", "tmp")
    return evaluate_local_project(f"{TMP}/{name}")


def print_evaluation_results(findings, owner, name):
    print()
    print("############ Analysis Results #############")
    print()

    for linter in linters:
        file_findings = get_findings_for_linter(linter.NAME, findings, True)
        content_findings = get_findings_for_linter(linter.NAME, findings)
        if len(file_findings) + len(content_findings) > 0:
            print(f"Linter: {linter.NAME}, Findings: {len(file_findings) + len(content_findings)}")
            if len(file_findings) > 0:
                print("File findings:")
                for file_finding in file_findings:
                    print(file_finding.write(f"{owner}/{name}"))
            if len(content_findings) > 0:
                print("File content findings:")
                for content_finding in content_findings:
                    print(content_finding.write(f"{owner}/{name}"))
            print()
    print()
    print("########### End of Results ###########")


def evaluate_local_project(full_path):
    return find_signals(full_path)


if __name__ == '__main__':
    flag = sys.argv[1]
    if flag == "-g":
        print_evaluation_results(evaluate_github_repo(sys.argv[2], sys.argv[3]), sys.argv[2], sys.argv[3])
    elif flag == "-f":
        print_evaluation_results(evaluate_local_project(sys.argv[2]), sys.argv[3], sys.argv[4])
    else:
        print("Missing or wrong flag!")
    clear_tmp()
