NAME = "SonarQube"

file_regex = {
    "sonar-generic-coverage[.]xsd",                                                         # https://docs.sonarqube.org/latest/analysis/generic-test/
    "sonar-project.properties"                                                              # manual analysis
}

signal_words = {
    "SonarQube", "Sonarqube", "sonarqube", "SONARQUBE",                                     # name
    "SonarLint", "sonarlint", "SonarSource", "sonarsource",                                 # related names
    "SonarJava", "SonarCloud", "sonarcloud",                                                # related names
    "sonar[.]cluster", "sonar[.]host[.]url", "sonar[.]projectKey",                          # https://docs.sonarqube.org/latest/analysis/analysis-parameters/
    "sonar[.]projectName", "sonar[.]projectVersion", "sonar[.]login",                       # https://docs.sonarqube.org/latest/analysis/analysis-parameters/
    "sonar[.]password", "sonar[.]ws[.]timeout", "sonar[.]projectDescription",               # https://docs.sonarqube.org/latest/analysis/analysis-parameters/
    "sonar[.]links[.]ci", "sonar[.]links[.]issue", "sonar[.]links[.]scm",                   # https://docs.sonarqube.org/latest/analysis/analysis-parameters/
    "sonar[.]sources", "sonar[.]tests", "sonar[.]externalIssuesReportPaths",                # https://docs.sonarqube.org/latest/analysis/analysis-parameters/
    "sonar[.]working[.]directory", "sonar[.]scm[.]exclusions[.]disabled",                   # https://docs.sonarqube.org/latest/analysis/analysis-parameters/
    "sonar[.]analysis", "sonar[.]cpd", "sonar[.]log",                                       # https://docs.sonarqube.org/latest/analysis/analysis-parameters/
    "sonar[.]verbose", "sonar[.]scanner", "sonar[.]qualitygate",                            # https://docs.sonarqube.org/latest/analysis/analysis-parameters/
    "sonar[.]coverageReportPaths", "sonar[.]coverage[.]jacoco[.]xmlReportPaths",            # https://docs.sonarqube.org/latest/analysis/coverage/
    "sonar[.]junit[.]reportPaths",                                                          # https://docs.sonarqube.org/latest/analysis/coverage/
    "sonar.*jacoco",                                                                        # from manual evaluation
    "sonar-maven-plugin", "sonar-scanner-maven", "sonar[.]java[.]jdkHome"                   # https://github.com/SonarSource/sonar-scanner-maven
}

