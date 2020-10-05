import os


def get_project_path(path):
    """ Функция возвращает путь до корневой папки проекта """
    proj_name = 'arenadata_test'
    while os.path.split(path)[1] != proj_name:
        path = os.path.split(path)[0]
    return path
