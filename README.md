
## Запуск теста

Для успешного запуска тест-кейса требуется  [Python](https://www.python.org/) v3+.


```sh
git clone https://github.com/pyuscherbakov/b2c_tests // Скачать репозиторий
cd b2c_tests                                         // Перейти в директорию репозитория
pip install -r requirements.txt                      // Установить требуемые плагины python
pytest --alluredir=./allure-results                  // Запустить тесты и сформировать Allure отчет
allure serve allure-results                          // Открыть Allure отчет
```
