import pytest

from pages.main_page import MainPage


@pytest.mark.usefixtures('start_chrome')
class TestsMain:

    # Тест проверяет приветственное сообщение, если шаблон не установлен
    def test_no_template(self,
                         delete_all_templates,
                         refresh,
                         ):
        mp = MainPage()
        mp.check_no_template_text('No template uploaded or your template is empty...')


    # Тест проверяет соответствие элементов в шаблоне элементам в DOM дереве
    def test_template(self,
                      upload_test_templates,
                      install_template_4,
                      refresh,
                      ):
        mp = MainPage()
        mp.check_template(install_template_4)
