
## Запуск тестов

Для успешного запуска тестов требуется  [Python](https://www.python.org/) v3+.

Bash скрипт для запуска:
```sh
#!/bin/bash
git clone https://github.com/pyuscherbakov/b2c_tests 
cd b2c_tests                                         
pip install -r requirements.txt                      #Установить требуемые плагины python
pytest -n=auto --alluredir=./allure-results          #Запустить все тесты и сформировать Allure отчет
allure serve allure-results                          #Открыть Allure отчет
```
