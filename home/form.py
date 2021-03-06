from django import forms
from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import logging
logger = logging.getLogger(__name__)

# noinspection PyUnresolvedReferences
class UserNameField(forms.CharField):
    def __init__(self, fieldname, *args, **kwargs):
        super(UserNameField, self).__init__(*args, **kwargs)
        self.fieldname = fieldname
        
    def to_python(self, value):
        if (not value) or (' ' in value):
            raise forms.ValidationError(
                    _('Invalid username %(value)s'),
                    code='invalid username',
                    params={'value': value},)
        else:
            return value
        
    def validate(self, value):
        if self.fieldname == 'register':
            if User.objects.filter(username=value).exists():
                raise forms.ValidationError(
                        _('The username %(value)s already exist!'),
                        code='duplicate username',
                        params={'value': '43'},)
        elif self.fieldname == 'signin':
            pass
        else:
            pass


class PassworField(forms.CharField):
    def __init__(self, fieldname, *args, **kwargs):
        super(PassworField, self).__init__(*args, **kwargs)
        self.fieldname = fieldname
        
    def to_python(self, value):
        if not value:
            raise forms.ValidationError(
                    _('The %(field)s is mandatory'),
                    code='field mandatory',
                    params={'field': self.fieldname},)
        else:
            return value


class RegisterForm(forms.Form):
    id_username_r = UserNameField(fieldname='Username', max_length=100, required=False)
    id_password_r = PassworField(fieldname='Password', widget=forms.PasswordInput())
    id_password_r_r = PassworField(fieldname='Retype password', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("id_password_r")
        confirm_password = cleaned_data.get("id_password_r_r")
        logger.error("password %s" , password)
        logger.error("confirm_password %s", confirm_password)
        return cleaned_data


class SignInForm(forms.Form):
    user_name = UserNameField(fieldname='signin', max_length=100, required=False)
    password = PassworField(fieldname='Password', widget=forms.PasswordInput())