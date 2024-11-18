# Python_Homework

**Запустить тесты и указать путь к каталогу результатов тестирования:**
```
pytest --alluredir allure-result
```
или
```
python -m pytest --alluredir allure-result
```
В директории с тестами появится папка allure-result. Там сохранятся отчеты о тестах.

Команда ниже запускает Allure и конвертирует результаты теста в отчет:
```
allure serve allure-result
```
Отчет откроется на локальном сервере в окне вашего браузера.