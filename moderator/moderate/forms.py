from django import forms
from models import Question


Q_PLACEHOLDER = 'What feedback do you have in regards to a move to Gmail? (in 300 chars)'


class QuestionForm(forms.ModelForm):
    """Question Form."""
    class Meta:
        model = Question
        fields = ['question']
        widgets = {
            'question': forms.TextInput(attrs={'placeholder': Q_PLACEHOLDER,
                                               'maxlength': '300'})
            }
