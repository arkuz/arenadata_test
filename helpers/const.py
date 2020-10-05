import os

from helpers.tools import get_project_path


# Пути к директориям
PROJECT = get_project_path(os.getcwd())  # корневая папка проекта
TEST_DATA = os.path.join(PROJECT, 'test_data')  # папка с тестовыми данными
