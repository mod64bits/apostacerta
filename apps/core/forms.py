from django import forms
from .models import Jogo


class JogosForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = '__all__'

    def clean(self):
        # data from the form is fetched using super function
        super(JogosForm, self).clean()
        print()

        return self.cleaned_data
