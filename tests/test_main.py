import tempfile
import unittest
from pathlib import Path
from main import parse_report, summarize

class DurationReportTests(unittest.TestCase):
    def test_sorts_slowest_first_and_totals(self):
        xml = '<testsuite><testcase name="fast" classname="A" time="0.2"/><testcase name="slow" classname="A" time="1.5"><failure/></testcase></testsuite>'
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/"junit.xml"
            path.write_text(xml, encoding="utf-8")
            tests = parse_report(path)
            report = summarize(tests)
        self.assertEqual(tests[0]["name"], "slow")
        self.assertEqual(report["test_count"], 2)
        self.assertEqual(report["total_seconds"], 1.7)
        self.assertTrue(tests[0]["failed"])

if __name__ == "__main__":
    unittest.main()
