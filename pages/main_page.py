from selene.support.shared.jquery_style import *
from selene import be, have


class MainPage(object):

    NO_TEMPLATE_TEXT = 'h3'
    ACTIVE_BTN = 'div.form-group > a'
    INACTIVE_BTN = 'div.form-group > button'

    def _get_depend_locator(self, id):
        return f"//*[name()='a' or name()='button']/parent::*[@id='{id}']"


    def check_no_template_text(self, text):
        s(self.NO_TEMPLATE_TEXT).should(have.text(text))


    def check_template(self, template_as_dict):
        for item in template_as_dict:
            id = item.get('id')
            label = item.get('label')
            link = item.get('link')
            depends = item.get('depends')

            if link:
                s(self.ACTIVE_BTN).should(have.attribute('href', link))
                s(self.ACTIVE_BTN).should(have.text(label))
                s(self.ACTIVE_BTN).should(have.attribute('id', str(id)))
            else:
                s(self.INACTIVE_BTN).should(have.text(label))
                s(self.INACTIVE_BTN).should(have.attribute('id', str(id)))
                s(self.INACTIVE_BTN).should(have.attribute('class', 'btn btn-primary disabled'))

            if depends:
                s(self._get_depend_locator(id)).should(be.visible)
