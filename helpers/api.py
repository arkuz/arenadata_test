import requests as req


class API():
    """ Класс описывает endpoints API """

    def __init__(self, url):
        self.url = url


    def _call_put_api(self, url, files, data={}):
        """ Обертка над requests.put """
        resp = req.put(
            url,
            files=files,
            data=data,
        )
        return resp


    def _call_post_api(self, url, data={}):
        """ Обертка над requests.post """
        resp = req.post(
            url,
            data=data,
        )
        return resp


    def _call_get_api(self, url, params={}):
        """ Обертка над requests.get """
        resp = req.get(
            url,
            params=params,
        )
        return resp


    def _call_delete_api(self, url, params={}, data={}):
        """ Обертка над requests.delete """
        resp = req.delete(
            url,
            data=data,
            params=params,
        )
        return resp


    def upload_template(self, filename, data={}):
        files = {'file': open(filename, 'rb')}
        endpoint = '/templates'
        url = self.url + endpoint
        return self._call_put_api(url, files=files, data=data)


    def get_templates(self):
        endpoint = '/templates'
        url = self.url + endpoint
        return self._call_get_api(url)


    def delete_template(self, tmpl_id):
        endpoint = f'/templates/{tmpl_id}'
        url = self.url + endpoint
        return self._call_delete_api(url)


    def insall_template(self, tmpl_id):
        endpoint = f'/templates/{tmpl_id}/install'
        url = self.url + endpoint
        return self._call_post_api(url)
