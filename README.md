# pytest-selenium-demoqa
Small AQA framework for https://demoqa.com/ 

Developed with **selenium**, **pytest** and **allure**

# Setup
1. `$ pip install -r requirements.txt`
2. [Allure Installation](https://allurereport.org/docs/gettingstarted-installation/)
3. `$ Set-Alias allure "path_to_installed_allure"` 
4. Run tests `$ pytest --alluredir=./tests/allure_results ./`
5. Get Allure report `$ allure serve .\tests\allure_results`
