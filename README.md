<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0d9488&height=170&section=header&text=Test%20Duration%20Report&fontSize=40&fontColor=ffffff&animation=fadeIn" width="100%" alt="Test Duration Report banner">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=21&pause=900&color=2DD4BF&center=true&vCenter=true&width=700&lines=Find%20the%20slowest%20tests%20in%20JUnit%20XML" alt="Animated project title">
</p>
<p align="center">
<a href="https://github.com/CyberLoop-dev/test-duration-report/blob/main/LICENSE"><img src="https://img.shields.io/github/license/CyberLoop-dev/test-duration-report?style=flat-square" alt="License"></a>
<img src="https://img.shields.io/badge/language-Python-0d9488?style=flat-square" alt="Python">
<a href="https://github.com/CyberLoop-dev/test-duration-report/stargazers"><img src="https://img.shields.io/github/stars/CyberLoop-dev/test-duration-report?style=flat-square" alt="Stars"></a>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/test-duration-report?style=flat-square" alt="Last commit">
</p>
<p align="center"><img src="assets/icon.svg" width="520" alt="Test Duration Report illustration"></p>

## 🧭 Overview
Parse JUnit XML test results and produce a compact report of slow tests and duration totals.

## ✨ Features
- ⏱️ Rank individual tests by execution time.
- 🧩 Summarize durations by test class or suite.
- 📤 Export machine-readable JSON for CI pipelines.
- 🧪 Work with common JUnit and pytest XML reports.

## 🖥️ Demo
~~~bash
python main.py examples/junit.xml --limit 5
~~~
Try it with the included sample input or your own local files.

## 🚀 Quick Start
~~~bash
git clone https://github.com/CyberLoop-dev/test-duration-report.git
cd test-duration-report
python main.py examples/junit.xml --limit 5
~~~

## 🧰 Tech Stack
- Python 3.10+
- xml.etree.ElementTree, argparse, json (standard library)

## 🗂️ Folder Structure
~~~text
test-duration-report/\n├── assets/icon.svg\n├── examples/junit.xml\n├── tests/test_main.py\n├── LICENSE\n├── README.md\n├── main.py\n└── requirements.txt
~~~

## 🗺️ Roadmap
- [ ] Add HTML report output.
- [ ] Add configurable slow-test thresholds.

## 🤝 Contributing
Issues and focused pull requests are welcome. Add tests for behavior changes and keep the project easy to run locally.

## 📄 License
Released under the MIT License. See LICENSE.

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d9488,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer"></p>
