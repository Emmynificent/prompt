from django.forms import ModelForm

from promptapp.models import Prompt

class PromptForm(ModelForm):
    class Meta:
        model = Prompt
        fields = '__all__'