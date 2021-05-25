NAME = "Blacklist"

file_regex = {}

signal_words = {
    "Static Analysis Tool", "static analysis tool",                         # might hint at a tool
    "Codacy", "codacy",                                                     # https://www.codacy.com/
    "Coverity", "coverity",                                                 # https://scan.coverity.com/
    "JArchitect", "jarchitect",                                             # https://www.jarchitect.com/
    "Jtest", "jtest", "Parasoft",                                           # https://www.parasoft.com/products/parasoft-jtest/java-static-analysis/
    "LDRA Testbed",                                                         # https://ldra.com/aerospace-defence/products/ldra-testbed-tbvision/
    "RIPSTECH", "RIPS-TECH", "RIPS",                                        # https://www.sonarsource.com/why-us/full-experience/?redirect=rips
    "Kiuwan", "kiuwan",                                                     # https://www.kiuwan.com/
    "Reshift", "reshift", "reshiftsecurity",                                # https://www.reshiftsecurity.com/
    "Embold", "embold",                                                     # https://embold.io/
    "SmartBear", "SMARTBEAR", "smartbear",                                  # https://smartbear.com/
    "CodeScene", "Codescene", "codescene",                                  # https://codescene.com/
    "VISUAL EXPERT", "Visual Expert", "visual expert", "visual-expert",     # https://www.visual-expert.com/EN/lp-ve-download-source_adv914ve.html
    "Veracode", "veracode",                                                 # https://www.veracode.com/security/static-analysis-tool
    "Fortify", "fortify",                                                   # https://www.microfocus.com/en-us/cyberres/application-security/static-code-analyzer
    "Hfcca", "hfcca"                                                        # https://code.google.com/archive/p/headerfile-free-cyclomatic-complexity-analyzer/
}