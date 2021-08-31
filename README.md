<td><img src="https://raw.githubusercontent.com/KorbiQWeidinger/LinterDetectionTool/master/static/ldt-logo.png" width="400px" /></td>

<b>Welcome to the LinterDetectionTool repository!</b> <br>
My name is Korbinian Weidinger and I'm a student at [TUM](https://www.tum.de/).

My [Bachelor Thesis](https://raw.githubusercontent.com/KorbiQWeidinger/LinterDetectionTool/master/static/thesis/BT_Korbinian_Weidinger.pdf) on <b>"Analysis of the Impact of Static AnalysisTools on the Code Quality of Open-SourceSoftware"</b>
requires me to automatically detect static analysis tools (linters) in OSS projects.

## Implementation background

There is no single unique indicator that allows a clear, indisputable assessment of the usage of a linter within
a project. Therefore, one can not automatically tell with one hundred percent certainty if a linter is in use 
in the development process of a project. Hence, the tool does not directly state if a linter is being used but
generates <b>findings</b> indicating the utilization of a certain linter within a project.

A finding is caused by <b>signals</b> that could indicate linter usage.
We search repositories filenames and contents for such signals.
Each signal references a linter. All signals can be found in src/constants/linters. 
The filename references the linter the signal indicates.

Additionally, there exists a [whitelist](https://raw.githubusercontent.com/KorbiQWeidinger/LinterDetectionTool/master/src/constants/file_regex_whitelist.py) of regular expressions for filenames.
We only search a files contents for signals if its name contains one of the regular expressions from the list.
We do this to avoid the generation of false positives.

More details can be found in Chapter 

## Integrated linters

Currently, we only integrate linters that support Java.


