# Pytest-BDD-UI-Automation
This project provides an example for testing a UI with Selenium WebDriver, written in Python, using the Page Object Model design pattern and driven via BDD feature files through Pytest BDD.

## Getting Started
1. Install [Poetry](https://python-poetry.org/docs/#installation) python dependency manager
2. Install [Docker](https://docs.docker.com/engine/install/) 
3. [Clone](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#clone-repo) this repository
4. Open the [terminal](https://www.jetbrains.com/help/pycharm/terminal-emulator.html#open-terminal) in pycharm, install the dependencies for the project using the following command
    ```
    poetry install
    ```
### Setting up Selenium Grid
```shell script
# Arm Machines (M1 Apple Compatible)
docker compose -f docker-compose-arm.yml up seleniarm-hub node-chrome

# x86 Machines
docker compose -f docker-compose.yml up selenium-hub node-chrome
```

```shell script
# Accessing Selenium Grid UI
http://127.0.0.1:4444/ui
```

### Setting up Allure Docker Service/ UI
```shell script
# Arm Machines (M1 Apple Compatible)
docker compose -f docker-compose-arm.yml up allure allure-ui

# x86 Machines
docker compose -f docker-compose.yml up allure allure-ui
```
```shell script
# Accessing Allure UI
http://localhost:5252/allure-docker-service-ui/
```
### Running Tests

```shell script
# All Tests
pytest
# Run Specific Test Stepfile
pytest pytest_bdd_ui_automation/steps/test_home_page_steps.py
```
