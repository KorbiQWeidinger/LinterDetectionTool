NAME = "SpotBugs"

file_regex = {
    ".*spotbugs.*",                                                               # name
    "spotbugs-exclude[.]xml",                                                     # ??
    "spotbugs-ant[.]jar",                                                         # https://spotbugs.readthedocs.io/en/latest/ant.html
    "sb-contrib-.*[.]jar"                                                         # https://github.com/mebigfatguy/fb-contrib
}

signal_words = {
    "spotbugs", "SpotBugs", "Spotbugs",                                         # name
    "sb-contrib", "com[.]mebigfatguy[.]sb-contrib",                             # https://github.com/mebigfatguy/fb-contrib
    "spotbugs-maven-plugin", "com[.]github[.]spotbugs",                         # https://spotbugs.readthedocs.io/en/latest/maven.html
    "findsecbugs", "Find Security Bugs"                                         # https://find-sec-bugs.github.io/
}
