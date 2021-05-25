NAME = "FindBugs"

file_regex = {
    ".*findbugs.*",                                                             # name
    "findbugs-exclude.xml",                                                     # ??
    "fb-contrib-.*.jar"                                                         # https://github.com/mebigfatguy/fb-contrib
}

signal_words = {
    "findbugs", "FindBugs", "Findbugs",                                         # name
    "fb-contrib", "com.mebigfatguy.fb-contrib", "findbugsPlugins",              # https://github.com/mebigfatguy/fb-contrib
    "com.google.code.findbugs:findbugs",                                        # https://github.com/mebigfatguy/fb-contrib
    "configurations.findbugsPlugins.dependencies",                              # https://github.com/mebigfatguy/fb-contrib
    "com.mebigfatguy.fb-contrib:fb-contrib",                                    # https://github.com/mebigfatguy/fb-contrib
    "project.configurations.findbugsPlugins"                                    # https://github.com/mebigfatguy/fb-contrib
}
