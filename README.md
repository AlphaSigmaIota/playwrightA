# playwrightA
Test automation project with python and playwright.

How to setup:
1) pip install -r requirements.txt
2) playwright install

How to use:
1) Check playwright is working properly with running file "check_playwright.py"
    You should see a chrome instance openes the official playwright.dev website
2) Run tests
    Just run the test_navigation.py as pytest > Two tests get's running
3) There are some files for pre-commit checks
    .pre-commit-config.yaml >> has 4 hooks inside for pre-commit checks
    .flake8 >> configuration file for flake8
    2x pyproject.toml >> configration for black and one file for interrogate
    
    You can install the pre-commit checks with:
    1) enable the lines in the requirements.txt
    2) run "pip install -r requirements.txt"
    3) run "pre-commit install" >> the pre-commit hooks get's installed
    4) make some code changes and try it out. This will ensure a high quality of your code!!


Have FUN!
