from django import forms


class ChatMessageForm(forms.Form):
    signature = forms.CharField()
    text = forms.CharField()
