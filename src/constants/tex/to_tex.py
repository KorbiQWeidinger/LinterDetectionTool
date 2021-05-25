from src.linter.constants import checkstyle, findbugs, pmd, semgrep, spotbugs

from src.linter.constants import blacklist, checkstyle, conqat, findbugs, infer, moose, pmd, pvs_studio, semgrep, \
    semmle, sonarqube, spotbugs

linters = {blacklist, checkstyle, conqat, findbugs, infer, moose, pmd, pvs_studio, semgrep, semmle, sonarqube, spotbugs}

if __name__ == '__main__':
    for linter in linters:
        print("%%%%%%%%%%%%%%%%%%%%%%%% " + linter.NAME + " %%%%%%%%%%%%%%%%%%%%%%%%%")
        print("\\vspace{10mm}\n\n" +
              "\\textbf{" + linter.NAME + "}\n\n" +
              "\\vspace{2mm}\n\n" +
              "Filenames:\n\n" +
              "\\vspace{1mm}\n\n" +
              "\\begin{lstlisting}")
        for name in linter.file_regex:
            print(name + ", ")
        print("\\end{lstlisting}\n\n" +
              "\\vspace{2mm}\n\n" +
              "File Content:\n\n" +
              "\\vspace{1mm}\n\n" +
              "\\begin{lstlisting}")
        for name in linter.signal_words:
            print(name + ", ")
        print("\\end{lstlisting}\n\n")
