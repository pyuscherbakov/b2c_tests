## Тесты API b2c 

Реализованы тесты следующих методов:
**Авторизация**
- Получить токен
**Аккаунт**
- Профиль
**Контракт**
- Создать контракт

## Запуск тестов

Для успешного запуска тестов требуется  [Python](https://www.python.org/) v3+.


```sh
git clone https://github.com/pyuscherbakov/b2c_tests 
cd b2c_tests                                         
pip install -r requirements.txt                      // Установить требуемые плагины python
pytest --alluredir=./allure-results                  // Запустить все тесты и сформировать Allure отчет
allure serve allure-results                          // Открыть Allure отчет
```
