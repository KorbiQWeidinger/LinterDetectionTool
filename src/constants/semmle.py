NAME = "Semmle"

file_regex = {
    ".*lgtm.*", ".*codeql.*",                                                  # names
    "lgtm-cluster-config.yml", ".*lgtm.*", "lgtm-config-gen.jar",              # https://help.semmle.com/lgtm-enterprise/admin/help/lgtm-cluster-config.html
    "lgtm.yml"                                                                 # https://help.semmle.com/lgtm-enterprise/admin/help/defining-global-project-config.html
}

signal_words = {
    "Semmle", "semmle",                                                         # name
    "LGTM", "CodeQL", "lgtm.", "codeql",                                        # Products
    "lgtm-controller", "lgtm-workerhost",                                       # https://help.semmle.com/lgtm-enterprise/ops/lgtm-enterprise-1270-system-architecture.pdf
    "LGTM_CREDENTIALS_PASSWORD", "LGTM_RAM", "LGTM_THREADS",                    # https://help.semmle.com/lgtm-enterprise/admin/help/environment-variables.html
    "lgtm-build-requirements", "lgtm-cli", "lgtm-down",                         # https://help.semmle.com/lgtm-enterprise/admin/help/section-commands.html
    "lgtm-import-ssl-certificate", "lgtm-status", "lgtm-upgrade"                # https://help.semmle.com/lgtm-enterprise/admin/help/section-commands.html
}
