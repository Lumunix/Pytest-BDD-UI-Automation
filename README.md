# Pytest-BDD-UI-Automation
This project provides an example for testing a UI with Selenium WebDriver, written in Python, using the Page Object Model design pattern and driven via BDD feature files through Pytest BDD. It can be used to kickstart testing of other UIs with minimal changes to the project.

NB This is not a complete implementation of a Selenium test suite for the target UI. It is an example of how to structure a Selenium test suite in Python but only a subset of the possible tests have been added.

## Getting Started
1. [Clone](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#clone-repo) this repository
2. Open the [terminal](https://www.jetbrains.com/help/pycharm/terminal-emulator.html#open-terminal) in pycharm, install the dependencies for the project using the following command
    ```
    poetry install
    ```
### Setting up Selenium Grid
```shell script
brew install socat
```
```shell script
socat -4 TCP-LISTEN:2375,fork UNIX-CONNECT:/var/run/docker.sock
```
```shell script
docker compose -f docker-compose-arm.yml up
```

