from django import forms
from models import Question


Q_PLACEHOLDER = 'Ask your question in 140 characters'
Q_ADMIN_PLACEHOLDER = 'Reply to question'


class QuestionForm(forms.ModelForm):
    """Question Form."""
    class Meta:
        model = Question
        fields = ['question']
        widgets = {
            'question': forms.TextInput(attrs={'placeholder': Q_PLACEHOLDER,
                                               'maxlength': '140'})
            }


class ReplyForm(forms.Form):
    """Reply Form."""
    reply = forms.CharField(max_length=140)
