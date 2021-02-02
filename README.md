**Requirements:**
1. Python 3.7 or higher
2. Packages from requirements.txt
3. (optional) Allure https://docs.qameta.io/allure/#_installing_a_commandline

**Usage:**
1. Run tests from project root and under virtual environment
2. To run tests on different environments use:  
    `pytest --env qa`  
    `pytest --env staging`  
    `pytest --env production`  
   'qa' environment is default parameter so can be omitted.
3. To run tests and generate allure report use:  
    `pytest --alluredir={dir}`  
    `allure serve {dir}`  
