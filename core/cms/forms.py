from django.contrib.auth.forms import (
    AuthenticationForm
)

class AuthenticationFormCustom(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for idx in self.fields:
            self.fields[idx].widget.attrs.update({
                'class': 'form-control',
                'placeholder': idx.title()
            })