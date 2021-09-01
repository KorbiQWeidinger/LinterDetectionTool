import os


def clear_and_create(folder):
    os.system(f'rm -rf {folder}')
    os.system(f'mkdir {folder}')


def get_findings_for_linter(linter_name, findings, file_findings=False):
    result = []
    for finding in findings:
        if finding.linter_name == linter_name:
            if finding.line == -1 and file_findings:
                result.append(finding)
            if finding.line != -1 and not file_findings:
                result.append(finding)
    return result