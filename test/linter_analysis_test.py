import unittest
import os

from src.linter_analysis import find_signals, save_findings_to_files

CWD = os.getcwd()
SAMPLE_PROJECT_PATH = CWD + "\\sample_project"
TMP_PATH = CWD + "\\tmp"


class LinterAnalysisTest(unittest.TestCase):

    def test_find_signals(self):
        result = find_signals(SAMPLE_PROJECT_PATH)
        self.assertEqual(12, len(result))

    def test_save_findings_to_files(self):
        os.system('mkdir ' + TMP_PATH)
        save_findings_to_files("Sample/Project", SAMPLE_PROJECT_PATH, TMP_PATH)
        self.assertTrue(os.path.exists(TMP_PATH + "\\Sample_Project+Blacklist+1.txt"))
        self.assertTrue(os.path.exists(TMP_PATH + "\\Sample_Project+Checkstyle+5.txt"))
        self.assertTrue(os.path.exists(TMP_PATH + "\\Sample_Project+FindBugs+1.txt"))
        self.assertTrue(os.path.exists(TMP_PATH + "\\Sample_Project+SpotBugs+3.txt"))
        self.assertTrue(os.path.exists(TMP_PATH + "\\Sample_Project+PMD+1.txt"))
        self.assertTrue(os.path.exists(TMP_PATH + "\\Sample_Project+Codacy+1.txt"))
        os.system('rmdir "%s" /s /q' % TMP_PATH)
