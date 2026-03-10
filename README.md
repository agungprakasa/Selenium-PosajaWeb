🤖 Selenium Web Automation Framework
Production-grade test automation for web applications — Python · Selenium · Jenkins · Docker

[Python 3.9+]  [Selenium 4.x]  [Jenkins CI]  [Docker]  [Allure Reports]  [MIT License]
/ ABOUT THIS PROJECT
This framework provides a scalable, maintainable automated testing solution for web applications. Built from hands-on experience at PT. Pos Indonesia testing Payment, Logistics, and Internal applications serving millions of users across Indonesia.

It follows Page Object Model (POM) architecture, integrates with Jenkins CI/CD pipeline, runs in Docker containers for consistent environments, and generates Allure HTML reports automatically.

Key Features
•Page Object Model (POM) — clean separation of test logic and UI selectors
•Parallel execution — run multiple test suites simultaneously, reducing total runtime
•Jenkins CI/CD integration — automated trigger on every Git push
•Docker support — containerized test execution, no environment setup needed
•Allure Reports — beautiful HTML reports with screenshots on failure
•Cross-browser support — Chrome, Firefox, Edge
•Data-driven testing — external test data via JSON/CSV/Excel

Tech Stack
Category	Tool	Purpose
Automation	Selenium WebDriver 4.x	Browser control & interaction
Language	Python 3.9+	Test scripting
Test Runner	pytest	Test execution & fixtures
CI/CD	Jenkins + GitLab CI	Automated pipeline
Container	Docker + Docker Compose	Consistent environments
Reporting	Allure Framework	HTML reports & screenshots
API Testing	Postman + Newman	API validation in CI
Security	OWASP ZAP	Vulnerability scanning
Code Quality	SonarQube	Static code analysis

Project Structure
selenium-framework/
├── tests/
│   ├── e2e/           ← End-to-end test suites
│   ├── api/           ← API test cases
│   └── regression/    ← Regression test suite
├── pages/             ← Page Object Model classes
├── utils/             ← Helpers, config, data loaders
├── reports/           ← Allure output (auto-generated)
├── docker/
│   └── Dockerfile     ← Container setup
├── Jenkinsfile        ← CI/CD pipeline definition
├── requirements.txt   ← Python dependencies
└── README.md
Quick Start
1. CLONE THE REPOSITORY
git clone https://github.com/agungprakasa/selenium-framework.git
2. INSTALL DEPENDENCIES
pip install -r requirements.txt
3. RUN WITH DOCKER (RECOMMENDED)
docker-compose up --build
4. VIEW ALLURE REPORT
allure serve reports/
Results & Impact
•30% reduction in manual regression testing time
•Integrated into GitLab CI — runs on every push to main branch
•Used in production for Posaja UMKM, Posaja Mobile, and Pospay SuperApp
•Supports 3 testing types: Functional, Regression, and UAT

Author
Agung Prakasa · Senior QA & DevSecOps Engineer · PT. Pos Indonesia
LinkedIn: linkedin.com/in/agung-prakasa-769b53137
Portfolio: agungprakasa.github.io/Myportfolio
