from pages.main_page import MainPage


class TestsMain:

    # Тест проверяет приветственное сообщение, если шаблон не установлен
    def test_no_template(self,
                         start_chrome,
                         delete_all_templates
                         ):
        mp = MainPage()
        mp.check_no_template_text('No template uploaded or your template is empty...')


    # Тест проверяет соответствие элементов в шаблоне элементам в DOM дереве
    def test_template(self,
                      start_chrome,
                      upload_test_templates,
                      install_template_4,
                      ):
        mp = MainPage()
        mp.check_template(install_template_4)
