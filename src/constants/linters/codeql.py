NAME = "CodeQL"

file_regex = {
    # ".*lgtm.*",                                                              # removed during manual analysis (only caused false positives)
    ".*codeql.*",                                                              # names
    "lgtm-cluster-config.yml", "lgtm-config-gen[.]jar",                        # https://help.semmle.com/lgtm-enterprise/admin/help/lgtm-cluster-config.html
    "lgtm[.]yml",                                                              # https://help.semmle.com/lgtm-enterprise/admin/help/defining-global-project-config.html
    "codeql-analysis.yml"                                                      # from manual analysis
}

signal_words = {
    # "LGTM", "lgtm[.]",                                                        # removed during manual analysis (only caused false positives)
    "CodeQL", "codeql",                                                         # name => only true positives from this
    "lgtm-controller", "lgtm-workerhost",                                       # https://help.semmle.com/lgtm-enterprise/ops/lgtm-enterprise-1270-system-architecture.pdf
    "LGTM_CREDENTIALS_PASSWORD", "LGTM_RAM", "LGTM_THREADS",                    # https://help.semmle.com/lgtm-enterprise/admin/help/environment-variables.html
    "lgtm-build-requirements", "lgtm-cli", "lgtm-down",                         # https://help.semmle.com/lgtm-enterprise/admin/help/section-commands.html
    "lgtm-import-ssl-certificate", "lgtm-status", "lgtm-upgrade"                # https://help.semmle.com/lgtm-enterprise/admin/help/section-commands.html
}
