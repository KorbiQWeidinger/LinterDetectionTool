import unittest
import os

from src.linter.analysis.linter_analysis import find_signal_words, find_files_and_folders, save_findings_to_files

CWD = os.getcwd()
SAMPLE_PROJECT_PATH = CWD + "\\sample_project"
TMP_PATH = CWD + "\\tmp"


class LinterAnalysisTest(unittest.TestCase):

    def test_find_signal_words(self):
        result = find_signal_words(SAMPLE_PROJECT_PATH)
        self.assertEqual(3, len(result))

    def test_find_files_and_folders(self):
        result = find_files_and_folders(SAMPLE_PROJECT_PATH)
        self.assertEqual(4, len(result))

    def test_save_findings_to_files(self):
        os.system('mkdir ' + TMP_PATH)
        save_findings_to_files("Sample/Project", SAMPLE_PROJECT_PATH, TMP_PATH)
        self.assertTrue(os.path.exists(TMP_PATH + "\\Sample_Project+Blacklist+2"))
        self.assertTrue(os.path.exists(TMP_PATH + "\\Sample_Project+Checkstyle+5"))
        self.assertTrue(os.path.exists(TMP_PATH + "\\Sample_Project+Findbugs+1"))
        os.system('rmdir "%s" /s /q' % TMP_PATH)
