from django import forms

class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput())
    retype_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("retype_password")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        return cleaned_data


class SignInForm(forms.Form):
    user_name = forms.CharField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput())