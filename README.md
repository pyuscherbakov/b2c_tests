## Тесты API b2c 

Реализованы тесты следующих методов:

1) Получить токен
2) Профиль
3) Создать контракт
4) Создать расчет
5) Получить расчет
6) Создать договор
7) Оформить договор
8) Договор– Получить выполнения текущей операции
9) Получить контракт
10) Обновить контракт

## Запуск тестов

Для успешного запуска тестов требуется  [Python](https://www.python.org/) v3+.

Bash скрипт для запуска:
```sh
#!/bin/bash
git clone https://github.com/pyuscherbakov/b2c_tests 
cd b2c_tests                                         
pip install -r requirements.txt                      #Установить требуемые плагины python
pytest -n=auto --alluredir=./allure-results                  #Запустить все тесты и сформировать Allure отчет
allure serve allure-results                          #Открыть Allure отчет
```
