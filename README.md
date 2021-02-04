# apiTest2

## Run test
\tests>pytest getTest.py

## Package list
pip freeze > requirements.txt
pip list



## Allure
Install allure-pytest
pytest getTest.py --alluredir ./reports
allure generate -c ./reports
allure serve ./reports        (optional)