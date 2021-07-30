NAME = "Blacklist"

threshold = 0

file_regex = {
    ".deepsource.toml"                                                                      # https://deepsource.io/features/
}

signal_words = {
    "Static Analysis Tool", "static analysis tool",                                         # might hint at usage of any SAT
    "JArchitect", "jarchitect",                                                             # https://www.jarchitect.com/
    "Jtest", "Parasoft",                                                                    # https://www.parasoft.com/products/parasoft-jtest/java-static-analysis/
    "LDRA Testbed",                                                                         # https://ldra.com/aerospace-defence/products/ldra-testbed-tbvision/
    "RIPSTECH", "RIPS-TECH", " RIPS ",                                                      # https://www.sonarsource.com/why-us/full-experience/?redirect=rips
    "Kiuwan", "kiuwan",                                                                     # https://www.kiuwan.com/
    " Reshift ", " reshift ", "reshiftsecurity",                                            # https://www.reshiftsecurity.com/ (created false positive from being embedded in words)
    " Embold ", " embold ",                                                                 # https://embold.io/ (created false positives from keyword "Embolden")
    "CodeScene", "Codescene", "codescene",                                                  # https://codescene.com/
    "VISUAL EXPERT", "Visual Expert", "visual expert", "visual-expert",                     # https://www.visual-expert.com/EN/lp-ve-download-source_adv914ve.html
    "Veracode", "veracode",                                                                 # https://www.veracode.com/security/static-analysis-tool
    "Fortify", " fortify",                                                                  # https://www.microfocus.com/en-us/cyberres/application-security/static-code-analyzer (issue due to https://fortify.net/)
    "fortify.ps.maven.plugin",                                                              # https://mvnrepository.com/artifact/com.fortify.ps.maven.plugin
    "Hfcca", "hfcca",                                                                       # https://code.google.com/archive/p/headerfile-free-cyclomatic-complexity-analyzer/
    "ConQAT", "conqat", "www.conqat.org",                                                   # https://www.cqse.eu/en/news/blog/conqat-end-of-life/
    "PVS-Studio", "pvs-studio", "pvsstudio", "PVSStudio",                                   # Linter moved to blacklist due to a lack in findings
    "pvs-studio-analyzer", "PVS_STUDIO_CORE", "pvsstudio-cores",                            # https://pvs-studio.com/en/docs/manual/0047/
    "PVS-Studio-Java", "SHORT_VERSION_PVS", "pvsAnalyze",                                   # https://pvs-studio.com/en/docs/manual/0047/
    "com[.]pvsstudio", "pvsstudio-maven-plugin",                                            # https://pvs-studio.com/en/docs/manual/
    "com[.]pvsstudio[.]PvsStudioGradlePlugin",                                              # https://pvs-studio.com/en/docs/manual/
    "MooseModel", "#mooseDisplayString", "moose[.]image", "moose.changes",                  # http://themoosebook.org/book/index.html#h1checkingandreportingwitharki
    "moosetechnology", "MooseDescription", "mooseDescription",                              # http://themoosebook.org/book/index.html#h1checkingandreportingwitharki
    "mooseModel", "mooseName", "MooseEntity",                                               # http://themoosebook.org/book/index.html#h1checkingandreportingwitharki
    "moosetechnology/Moose", "moosequery",                                                  # https://github.com/moosetechnology/Moose
    "semgrep", "Semgrep",                                                                   # Linter moved to blacklist due to a lack in findings
    "returntocorp/semgrep",                                                                 # Semgrep GitHub URL
    "SEMGREP_RULESET",                                                                      # https://semgrep.dev/docs/extensions/
    "semgrep-action", "semgrep-agent",                                                      # https://semgrep.dev/docs/semgrep-ci/
    "infer/", "/infer", "infer run", "infer-linux",                                         # https://fbinfer.com/docs/getting-started/
    "infer capture",                                                                        # https://fbinfer.com/docs/getting-started/
    "com[.]facebook[.]infer", "com[.]facebook[.]infer[.]annotation", "infer-annotation",    # https://mvnrepository.com/artifact/com.facebook.infer.annotation/infer-annotation/0.18.0
    "infer-maven-plugin",                                                                   # https://github.com/anthemengineering/infer-maven-plugin
    "com[.]uber:infer-plugin", "com[.]uber[.]infer[.]java",                                 # https://github.com/uber-archive/infer-plugin
    "com[.]uber[.]infer[.]android", "inferPlugin",                                          # https://github.com/uber-archive/infer-plugin
    "Jenkins-Android-Infer", "INFER_VERSION",                                               # https://github.com/umarniz/Jenkins-Android-Infer
    "DeepSource", "deepsource",                                                             # https://deepsource.io/
}

