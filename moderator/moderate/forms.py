from django import forms
from models import Question


Q_PLACEHOLDER = 'What are the things at Mozilla that keep you from getting work done? (max 250 characters)'


class QuestionForm(forms.ModelForm):
    """Question Form."""
    class Meta:
        model = Question
        fields = ['question']
        widgets = {
            'question': forms.TextInput(attrs={'placeholder': Q_PLACEHOLDER,
                                               'maxlength': '250'})
            }
