#!/usr/bin/env python3
"""Summarize slow tests from JUnit XML."""
import argparse
import json
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

def parse_report(path: Path):
    root = ET.parse(path).getroot()
    tests = []
    for node in root.iter("testcase"):
        try:
            duration = float(node.get("time", "0"))
        except ValueError:
            duration = 0.0
        tests.append({
            "name": node.get("name", "unnamed"),
            "suite": node.get("classname") or node.get("file") or "unknown",
            "seconds": max(0.0, duration),
            "failed": any(child.tag in {"failure", "error"} for child in node),
        })
    return sorted(tests, key=lambda item: item["seconds"], reverse=True)

def summarize(tests):
    groups = defaultdict(float)
    for item in tests:
        groups[item["suite"]] += item["seconds"]
    return {
        "test_count": len(tests),
        "total_seconds": round(sum(item["seconds"] for item in tests), 4),
        "by_suite": dict(sorted(groups.items(), key=lambda pair: pair[1], reverse=True)),
        "tests": tests,
    }

def main():
    parser = argparse.ArgumentParser(description="Report the slowest tests from JUnit XML.")
    parser.add_argument("xml", type=Path)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be at least 1")
    try:
        report = summarize(parse_report(args.xml))
    except (OSError, ET.ParseError) as exc:
        parser.error(str(exc))
    if args.as_json:
        print(json.dumps(report, indent=2))
        return
    print(f"{report['test_count']} tests · {report['total_seconds']:.3f}s total")
    for item in report["tests"][:args.limit]:
        status = "FAIL" if item["failed"] else "PASS"
        print(f"{item['seconds']:8.3f}s  {status:4}  {item['suite']} :: {item['name']}")
    print("\nSuite totals:")
    for suite, seconds in report["by_suite"].items():
        print(f"  {seconds:8.3f}s  {suite}")
if __name__ == "__main__":
    main()
