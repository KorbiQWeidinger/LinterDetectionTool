NAME = "Semgrep"

file_regex = {
    ".*semgrep.*",                                                                  # name
    ".semgrepignore",                                                           # https://semgrep.dev/docs/semgrep-ci/
    ".pre-commit-config.yaml",                                                  # https://semgrep.dev/docs/extensions/
    ".semgrep.yml"                                                              # https://semgrep.dev/docs/semgrep-ci/
}

signal_words = {
    "semgrep", "Semgrep",                                                       # name
    "returntocorp/semgrep",                                                     # GitHub URL
    "SEMGREP_RULESET",                                                          # https://semgrep.dev/docs/extensions/
    "semgrep-action", "semgrep-agent"                                           # https://semgrep.dev/docs/semgrep-ci/
}
