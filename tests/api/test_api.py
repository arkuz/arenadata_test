import pytest
import os

from helpers.api import API
from helpers.readers import read_yaml
import helpers.const as const


class TestsAPI:

    config = read_yaml(os.path.join(const.PROJECT, 'config.yaml'))
    api_url = config['api_url']
    api = API(api_url)


    # Тест на загрузку шаблона без дополнительных параметров
    @pytest.mark.parametrize('name', [
        'temp.yaml',
        '1.yaml',
    ])
    def test_upload_template_without_data(self, name):
        filename = os.path.join(const.TEST_DATA, name)
        resp = self.api.upload_template(filename=filename)
        assert resp.status_code == 201
        assert resp.json()['message'] == f'Template successfully uploaded. tmpl_id={name.split(".")[0]}'


    # Тест на загрузку шаблона с дополнительными параметрами
    @pytest.mark.parametrize('name', [
        'temp.yaml',
        'временный.yaml',
        '1.yaml'
    ])
    def test_upload_template_with_data(self, name):
        file = 'temp.yaml'
        data = {'data': '{"tmpl_id":"' + name.split(".")[0] + '"}'}
        filename = os.path.join(const.TEST_DATA, file)
        resp = self.api.upload_template(filename=filename, data=data)
        assert resp.status_code == 201
        assert resp.json()['message'] == f'Template successfully uploaded. tmpl_id={name.split(".")[0]}'


    # Тест на загрузку шаблона с неподдерживаемым расширегием файла
    @pytest.mark.parametrize('name', [
        'without_extention',
        'extention_pdf.pdf',
    ])
    def test_upload_template_invalid(self, name):
        filename = os.path.join(const.TEST_DATA, name)
        resp = self.api.upload_template(filename=filename)
        assert resp.status_code == 400
        msg = 'Allowed file types are '
        assert resp.json()['message'] == msg + "{'yml', 'yaml'}" \
               or resp.json()['message'] == msg + "{'yaml', 'yml'}"


    # Тест на получение всех загруженных шаблонов
    def test_get_templates(self,
                           delete_all_templates,
                           upload_test_templates
                           ):
        resp = self.api.get_templates()
        assert resp.status_code == 200
        assert resp.json()['templates'] == ['1', '2', '3', '4']


    # Тест на удаление существующего шаблона
    def test_delete_templates(self,
                              delete_all_templates,
                              upload_test_templates
                              ):
        templ_id = '1'
        resp = self.api.delete_template(templ_id)
        assert resp.status_code == 200
        assert resp.json()['message'] == f'Template with tmpl_id={templ_id} successfully deleted!'
        resp = self.api.get_templates()
        assert resp.json()['templates'] == ['2', '3', '4']


    # Тест на удаление НЕсуществующего шаблона
    def test_delete_templates_invalid(self):
        templ_id = 'not_exist_template_xxx'
        resp = self.api.delete_template(templ_id)
        assert resp.status_code == 404
        assert resp.json()['message'] == f'No template with tmpl_id={templ_id} found!'


    # Тест на установку шаблона
    def test_insall_templates(self,
                              delete_all_templates,
                              upload_test_templates
                              ):
        templ_id = '1'
        resp = self.api.insall_template(templ_id)
        assert resp.status_code == 200
        assert resp.json()['message'] == f'Template with tmpl_id={templ_id} successfully installed!'


    # Тест на установку шаблона? который ссылается на несуществующий объект
    def test_insall_templates_not_exist_id(self,
                                           delete_all_templates,
                                           upload_test_templates
                                           ):
        templ_id = '3'
        resp = self.api.insall_template(templ_id)
        assert resp.status_code == 500
        assert 'is not presented in template' in resp.json()['message']


    # Тест на установку НЕсуществующего шаблона
    def test_insall_templates_invalid(self):
        templ_id = 'not_exist_template_xxx'
        resp = self.api.insall_template(templ_id)
        assert resp.status_code == 404
        assert resp.json()['message'] == f'No template with tmpl_id={templ_id} found!'
