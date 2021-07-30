NAME = "Checkstyle"

threshold = 3

file_regex = {
    ".*checkstyle.*",                                                               # name
    "checkstyle[.]xml",                                                             # https://docs.gradle.org/current/userguide/checkstyle_plugin.html in <root>\config\checkstyle, https://stickler-ci.com/docs#java
    "google_checks[.]xml", "sun_checks[.]xml",                                      # https://github.com/nikitasavinov/checkstyle-action#checkstyle-github-action
    "checkstyle_config[.]xml",                                                      # https://github.com/nikitasavinov/checkstyle-action#checkstyle-github-action
    "maven_checks[.]xml",                                                           # http://maven.apache.org/plugins/maven-checkstyle-plugin/
    "linter[.]yml",                                                                 # https://github.com/github/super-linter in <root>/.github/workflows/
    "checkstyle-suppressions[.]xml"                                                 # from manual analysis
}

signal_words = {
    "Checkstyle", "checkstyle", "CheckStyle", "check style", "Check Style",     # name
    "maven-checkstyle-plugin",                                                  # http://maven.apache.org/plugins/maven-checkstyle-plugin/
    "checkstyle-action", "Run check style",                                     # https://github.com/nikitasavinov/checkstyle-action#checkstyle-github-action
    "checkstyleMain", "checkstyleTest", "checkstyleSourceSet",                  # https://docs.gradle.org/current/userguide/checkstyle_plugin.html
    "checkstyle:checkstyle", "checkstyle:checkstyle-aggregate",                 # http://maven.apache.org/plugins/maven-checkstyle-plugin/
    "checkstyle:check",                                                         # http://maven.apache.org/plugins/maven-checkstyle-plugin/
    "megalinter", "Mega-Linter", "mega-linter",                                 # https://github.com/nvuillam/mega-linter
    "superlinter", "Super-Linter", "super-linter",                              # https://github.com/github/super-linter
    "codacy-checkstyle", "checkstyleVersion"                                    # https://github.com/codacy/codacy-checkstyle/
}
