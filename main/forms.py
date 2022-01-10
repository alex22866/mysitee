from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]     #список
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите текст'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'введите описание'
            })
        }
