import sys


def evaluate_github_repo(repo_url):
    pass


def print_evaluation_results(result):
    pass


def evaluate_local_project(param):
    pass


if __name__ == '__main__':
    flag = sys.argv[1]
    if flag == "-g":
        print_evaluation_results(evaluate_github_repo(sys.argv[2]))
    elif flag == "-f":
        print_evaluation_results(evaluate_local_project(sys.argv[2]))
    else:
        print("Missing or wrong flag!")

