
## Запуск теста

Для успешного запуска тест-кейса требуется  [Python](https://www.python.org/) v3+.


```sh
git clone https://github.com/pyuscherbakov/b2c_tests
cd b2c_tests
pip install -r requirements.txt 
python3 -n=auto pytest --alluredir=./allure-results tests/
allure serve ./allure-results/
```
