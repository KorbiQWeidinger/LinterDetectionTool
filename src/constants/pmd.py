NAME = "PMD"

file_regex = {
    ".*pmd.*",
    "pmd.xml"                                                                   # https://docs.gradle.org/current/userguide/pmd_plugin.html
}

signal_words = {
    "pmd ", "PMD ", "\'pmd\'", "\"pmd\"", "pmd:", ".pmd", "pmd.",               # name (with spaces to avoid false positives)
    "Copy/Paste Detector", "copy-paste detector",                               # copy-paste detector add-on
    "pmdMain", "pmdTest", "pmdSourceSet", "net.sourceforge.pmd",                # https://docs.gradle.org/current/userguide/pmd_plugin.html (gradle tasks)
    "maven-pmd-plugin", "pmd-core", "pmd-java", "pmdVersion"                    # https://pmd.github.io/latest/pmd_userdocs_tools_maven.html
    "CPDTask", "CPD-START", "CPD-END",                                          # https://pmd.github.io/latest/pmd_userdocs_cpd.html
    "violationSuppressXPath",                                                   # https://pmd.github.io/latest/pmd_userdocs_suppressing_warnings.html
    "codacy-pmd", "codacy-pmdjava"                                              # https://github.com/codacy/codacy-pmd
}
