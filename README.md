# 🌐 Web Automation Framework — Selenium + Python

Automated web testing framework for enterprise web applications using **Selenium WebDriver** + **Python** + **pytest**, integrated with **Jenkins CI/CD** pipeline.

> Built and maintained by **Agung Prakasa** — Senior QA & DevSecOps Engineer  
> Production-tested on **Posaja UMKM**, **Posaja Mobile Web**, and **Pospay SuperApp** at PT. Pos Indonesia

---

## ✨ Key Features

- **Selenium WebDriver 4.x** — Latest web automation with relative locators & Chrome DevTools Protocol
- **pytest** — Powerful test runner with fixtures, parametrize, and plugins
- **Page Object Model (POM)** — Clean, maintainable, and scalable architecture
- **Allure Reports** — Beautiful HTML reports with screenshots, steps, and history
- **Docker Support** — Consistent test environments via containerized Selenium Grid
- **Jenkins CI/CD** — Automated pipeline triggered on every Git push
- **Cross-Browser** — Chrome, Firefox, Edge
- **Data-Driven Testing** — External test data via JSON / CSV / Excel
- **Auto Screenshot on Failure** — Captured and embedded in Allure report
- **SonarQube Integration** — Static code quality analysis in pipeline

---

## 📁 Project Structure

```
selenium-web-automation/
├── tests/
│   ├── e2e/
│   │   ├── test_login.py              # Login flow (7 TC)
│   │   ├── test_checkout.py           # Checkout flow (10 TC)
│   │   └── test_payment.py            # Payment flow (8 TC)
│   ├── regression/
│   │   ├── test_smoke.py              # Smoke test suite (5 TC)
│   │   └── test_full_regression.py    # Full regression (30+ TC)
│   └── conftest.py                    # pytest fixtures & hooks
├── pages/                             # Page Object Model
│   ├── base_page.py                   # Base class: common actions
│   ├── login_page.py
│   ├── home_page.py
│   ├── checkout_page.py
│   └── payment_page.py
├── utils/
│   ├── config.py                      # Environment config & base URL
│   ├── driver_factory.py              # WebDriver setup (local & Grid)
│   ├── screenshot.py                  # Screenshot helper
│   └── data_loader.py                 # JSON/CSV test data reader
├── data/
│   ├── users.json                     # Test user credentials
│   └── products.csv                   # Product test data
├── reports/                           # Allure output (auto-generated)
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml             # Selenium Grid setup
├── Jenkinsfile                        # CI/CD pipeline definition
├── sonar-project.properties           # SonarQube config
├── pytest.ini                         # pytest configuration
├── requirements.txt                   # Python dependencies
└── README.md
```

---

## ⚙️ Prerequisites

| Software      | Version  | Download |
|---------------|----------|----------|
| **Python**    | 3.9+     | [python.org](https://www.python.org/) |
| **Chrome**    | Latest   | [google.com/chrome](https://www.google.com/chrome/) |
| **ChromeDriver** | Match Chrome | [chromedriver.chromium.org](https://chromedriver.chromium.org/) |
| **Docker**    | 20.x+    | [docker.com](https://www.docker.com/) |
| **Allure CLI** | 2.x     | [docs.qameta.io](https://docs.qameta.io/allure/) |
| **Java JDK**  | 11+      | Required for Allure |

### Environment Variables

```bash
# .env file — copy from .env.example and fill in
BASE_URL=https://your-app-url.com
TEST_USERNAME=your_test_user
TEST_PASSWORD=your_test_password
BROWSER=chrome          # chrome | firefox | edge
HEADLESS=false          # true for CI
SELENIUM_GRID_URL=http://localhost:4444/wd/hub   # optional
```

---

## 🚀 Getting Started

### 1. Clone & Install

```bash
git clone https://github.com/agungprakasa/selenium-web-automation.git
cd selenium-web-automation
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run with Docker (Recommended)

```bash
# Start Selenium Grid + run tests in one command
docker-compose up --build

# Or run tests against existing Grid
docker-compose up -d selenium-hub chrome-node
pytest tests/ --grid
```

### 3. Run Locally

```bash
# Run all tests
pytest tests/

# Run specific suite
pytest tests/e2e/test_login.py -v

# Run with tags
pytest tests/ -m "smoke"
pytest tests/ -m "regression"

# Run parallel (4 workers)
pytest tests/ -n 4

# Run headless
HEADLESS=true pytest tests/
```

### 4. View Allure Reports

```bash
# Generate and open
allure serve reports/

# Generate static HTML
allure generate reports/ --clean -o allure-report/
```

---

## 🔧 Jenkins CI/CD Pipeline

The `Jenkinsfile` at the root defines a full automated pipeline:

```
Code Push → Install Deps → Lint (flake8) → Run Tests (parallel) → 
Allure Report → SonarQube Scan → Notify Slack → Deploy (on main)
```

### Jenkinsfile Preview

```groovy
pipeline {
    agent { docker { image 'python:3.9-slim' } }
    
    stages {
        stage('Install') {
            steps { sh 'pip install -r requirements.txt' }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/ -n 4 --alluredir=reports/ --junitxml=results.xml'
            }
            post {
                always { allure includeProperties: false, results: [[path: 'reports']] }
            }
        }
        stage('SonarQube') {
            steps { withSonarQubeEnv('sonar') { sh 'sonar-scanner' } }
        }
    }
    post {
        always { slackSend message: "Build ${currentBuild.result}: ${env.JOB_NAME}" }
    }
}
```

---

## 📊 Test Coverage

| # | Feature        | File                        | TCs | Scenarios |
|---|----------------|-----------------------------|-----|-----------|
| 1 | Login          | `test_login.py`             | 7   | Valid/invalid login, empty fields, remember me, locked account |
| 2 | Checkout       | `test_checkout.py`          | 10  | Add to cart, update qty, remove, coupon, proceed |
| 3 | Payment        | `test_payment.py`           | 8   | Card, bank transfer, e-wallet, failed payment |
| 4 | Smoke          | `test_smoke.py`             | 5   | Critical paths only |
| 5 | Full Regression | `test_full_regression.py`  | 30  | Complete app coverage |
|   | **Total**      |                             | **60** | |

---

## 🛠 Tech Stack

| Tool              | Purpose                         |
|-------------------|---------------------------------|
| **Selenium 4.x**  | Browser automation              |
| **Python 3.9+**   | Programming language            |
| **pytest**        | Test runner & fixtures          |
| **Allure**        | HTML reports with screenshots   |
| **Docker**        | Containerized test environments |
| **Jenkins**       | CI/CD pipeline                  |
| **SonarQube**     | Code quality analysis           |
| **flake8**        | Python linting                  |

---

## 📈 Results & Impact

> Applied in production at **PT. Pos Indonesia** across 3 major platforms

- ✅ **30% reduction** in manual regression testing time
- ✅ **20% fewer** post-release critical defects
- ✅ Integrated into GitLab CI — **runs on every push** to main branch
- ✅ **60+ automated test cases** covering Login, Payment, Logistics flows

---

## 👤 Author

**Agung Prakasa** — Senior QA & DevSecOps Engineer  
📧 agungprakasa49@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/agung-prakasa-769b53137/) · [Portfolio](https://agungprakasa.github.io/Myportfolio/) · [GitHub](https://github.com/agungprakasa)

---

*⭐ If this framework helps you, please give it a star!*
