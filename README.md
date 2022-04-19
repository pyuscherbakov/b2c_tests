## Тесты API b2c 

## Тесты API b2c 

Реализованы тесты следующих методов:

1) Получить токен
2) Профиль
3) Создать контракт
4) Создать расчет

## Запуск тестов

Для успешного запуска тестов требуется  [Python](https://www.python.org/) v3+.

Bash скрипт для запуска
```sh
#!/bin/bash
git clone https://github.com/pyuscherbakov/b2c_tests 
cd b2c_tests                                         
pip install -r requirements.txt                      #Установить требуемые плагины python
pytest --alluredir=./allure-results                  #Запустить все тесты и сформировать Allure отчет
allure serve allure-results                          #Открыть Allure отчет
```
