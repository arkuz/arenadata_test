### Тестовое задание на должность QA Automation Engineer в Arenadata
Задание здесь - [https://github.com/dgusakov/test_app](https://github.com/dgusakov/test_app)

### Требования к ПО
- Python 3.7 и старше - [www.python.org/getit/](https://www.python.org/getit/)
- Инструмент для работы с виртуальными окружениями virtualenv
```bash
pip install virtualenv
```
- Для web тестов используется библиотека selene. Скачивать webdriver и т.п. нет необходимости. Библиотека все сделает автоматически.

### Копирование репозитория и установка зависимостей
```bash
git clone https://github.com/arkuz/arenadata_tests
cd arenadata_tests
virtualenv env
env/bin/activate
pip install -r requirements.txt
```

### Запуск тестов
 - Перед запуском тестов необходимо перейти в каталог проекта `arenadata_tests`
 
Аргументы запуска:
- -s - показывать принты в процессе выпонения
- -v - verbose режим, чтобы видеть, какие тесты были запущены

##### Запуск всех тестов
```bash
py.test -s -v tests
```

##### Запуск API тестов 
```bash
py.test -s -v tests/api
```

##### Запуск web тестов 
```bash
py.test -s -v tests/web
```

#### Результат выполнения
```bash
============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-6.1.0, py-1.9.0, pluggy-0.13.1 -- C:\Users\arkuz\AppData\Local\Programs\Python\Python37-32\python.exe
cachedir: .pytest_cache
rootdir: D:\GitHub\arenadata_test, configfile: pytest.ini
collecting ... collected 14 items

test_api.py::TestsAPI::test_upload_template_without_data['temp.yaml'] 
test_api.py::TestsAPI::test_upload_template_without_data['1.yaml'] 
test_api.py::TestsAPI::test_upload_template_with_data['temp.yaml'] 
test_api.py::TestsAPI::test_upload_template_with_data['временный.yaml'] 
test_api.py::TestsAPI::test_upload_template_with_data['1.yaml'] 
test_api.py::TestsAPI::test_upload_template_invalid['without_extention'] 
test_api.py::TestsAPI::test_upload_template_invalid['extention_pdf.pdf'] 
test_api.py::TestsAPI::test_get_templates 
test_api.py::TestsAPI::test_delete_templates 
test_api.py::TestsAPI::test_delete_templates_invalid 
test_api.py::TestsAPI::test_insall_templates 
test_api.py::TestsAPI::test_insall_templates_not_exist_id 
test_api.py::TestsAPI::test_insall_templates_invalid 
test_api.py::TestsAPI::test_insall_empty_template_invalid 

============================= 14 passed in 1.01s ==============================
```