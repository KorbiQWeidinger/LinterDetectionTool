NAME = "FindBugs"

file_regex = {
    ".*findbugs.*",                                                                 # name
    "findbugs-exclude[.]xml",                                                       # from analysis
    "fb-contrib-.*[.]jar",                                                          # https://github.com/mebigfatguy/fb-contrib
    "[.]fbprefs"
}

signal_words = {
    "findbugs", "FindBugs", "Findbugs", "FINDBUGS",                                     # name
    "fb-contrib", "com[.]mebigfatguy[.]fb-contrib", "findbugsPlugins",                  # https://github.com/mebigfatguy/fb-contrib
    "com[.]google[.]code[.]findbugs",                                                   # https://github.com/mebigfatguy/fb-contrib
    "configurations[.]findbugsPlugins[.]dependencies",                                  # https://github.com/mebigfatguy/fb-contrib
    "com[.]mebigfatguy[.]fb-contrib:fb-contrib",                                        # https://github.com/mebigfatguy/fb-contrib
    "project[.]configurations[.]findbugsPlugins",                                       # https://github.com/mebigfatguy/fb-contrib
    "findbugs-maven-plugin",
    "findbugsVersion"
}
