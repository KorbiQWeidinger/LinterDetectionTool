<td><img src="https://raw.githubusercontent.com/KorbiQWeidinger/LinterDetectionTool/master/static/ldt-logo.png" width="400px" /></td>

<b>Welcome to the LinterDetectionTool repository!</b> <br>
My name is Korbinian Weidinger and I'm a student at [TUM](https://www.tum.de/).

My [Bachelor Thesis](https://raw.githubusercontent.com/KorbiQWeidinger/LinterDetectionTool/master/static/thesis/BT_Korbinian_Weidinger.pdf) on 
<b>"Analysis of the Impact of Static AnalysisTools on the Code Quality of Open-SourceSoftware"</b>
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

More details can be found in <b>Chapter 3.5 LinterDetectionTool</b> in my [Bachelor Thesis](https://raw.githubusercontent.com/KorbiQWeidinger/LinterDetectionTool/master/static/thesis/BT_Korbinian_Weidinger.pdf).

## Usage guide

### Flask app

The implementation includes a flask web app to easily allow manual inspection of findings.

<b>Run flask app locally:</b> `flask run` and access it under [http://localhost:5000/](http://localhost:5000/)

We are working on hosting a flask application (for free) so you can try and use the 
LinterDetectionTool without cloning. Sadly we are facing issues with free servers and their 
allowed download capacities since project analysis requires us to download a repository.

We currently host the app via [Heroku](https://www.heroku.com/home) and the app can be found [here](https://linter-detection-tool.herokuapp.com/). <br>
Sadly it is not functional jet!

### CLI

You can execute the LinterDetectionTool by running the following commands. <br>

To clone and analyse a publicly available git repository run: <br>
```
python3 ldt-cli.py -g https://github.com/<owner>/<repo_name>.git
```

To analyse a project on your machine: <br>
```
python3 ldt-cli.py -f <full_path>
```

## Integrated linters

Currently, we only integrate linters that support Java.

The integrated linters are:

<table>
<tbody style="text-align: center">
<tr>
<td><img style="background: aliceblue" src="https://checkstyle.sourceforge.io/images/header-checkstyle-logo.png" alt="" width="120" /></td>
<td><img src="https://pmd.github.io/img/pmd_logo.png" alt="" width="120" /></td>
<td><img src="https://www.sonarqube.org/assets/logo-31ad3115b1b4b120f3d1efd63e6b13ac9f1f89437f0cf6881cc4d8b5603a52b4.svg" alt="" width="120" /></td>
<td><img src="https://spotbugs.github.io/images/logos/spotbugs_icon_only_zoom_256px.png" alt="" width="120" /></td>
</tr>
<tr>
<td><em><a href="https://checkstyle.sourceforge.io/">Checkstyle</a></em></td>
<td><em><a href="https://pmd.github.io/">PMD</a></em></td>
<td><em><a href="https://www.sonarqube.org/">SonarQube</a></em></td>
<td><em><a href="https://spotbugs.github.io/">SpotBugs</a></em></td>

</tr>
<tr>
<td><img src="http://findbugs.sourceforge.net/umdFindbugs.png" alt="" width="120" /></td>
<td><img src="https://avatars.githubusercontent.com/ml/1714?s=140&v=4" alt="" width="120" /></td>
<td><img src="https://www.codacy.com/landing-page-assets/images/codacy-logo.svg" alt="" width="120" /></td>
<td><img src="https://scan.coverity.com/assets/synopsys-navbar-logo-b2b5c7d76e6473caf95bcc9dc83fb53324427384cde4d9ffd728ea616599c6da.png" alt="" width="120" /></td>
</tr>
<tr>
<td><em><a href="http://findbugs.sourceforge.net/">FindBugs</a></em></td>
<td><em><a href="https://fbinfer.com/">Semmle (LGTM & CodeQL)</a></em></td>
<td><em><a href="https://www.codacy.com/">Codacy</a></em></td>
<td><em><a href="https://scan.coverity.com/">Coverity</a></em></td>
</tr>
</tbody>
</table>


Linters that we had difficulties detecting (findings created by signals on the blacklist): 

<table>
<tbody style="text-align: center">
<tr>
<td><img src="https://fbinfer.com/img/logo.png" alt="" width="120" /></td>
<td><img src="https://raw.githubusercontent.com/returntocorp/semgrep/develop/semgrep.svg" alt="" width="120" /></td>
<td><img src="https://moosetechnology.org/pictures/moose-icon.png" alt="" width="120" /></td>
</tr>
<tr>
<td><em><a href="https://fbinfer.com/">Infer</a></em></td>
<td><em><a href="https://semgrep.dev/">Semgrep</a></em></td>
<td><em><a href="https://moosetechnology.org/">Moose</a></em></td>
</tr>
</tbody>
</table>
