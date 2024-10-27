from django import forms
from . import models

class FeedbackForm(forms.Form):
    username =forms.CharField(max_length=100)
    feedback =forms.CharField(widget=forms.Textarea, required=True)