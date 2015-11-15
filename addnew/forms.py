__author__ = 'Jasmeet'
from django import forms
from addnew.models import add,Message

class addform(forms.ModelForm):
    fname=forms.CharField(widget=forms.HiddenInput())
    mobile=forms.IntegerField(widget=forms.HiddenInput())
    email=forms.EmailField(widget=forms.HiddenInput())
    dob=forms.DateField(widget=forms.HiddenInput())
    marriageaniversary=forms.DateField(widget=forms.HiddenInput())
    remarks=forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model=add
        fields = ['fname','mobile','email','dob','marriageaniversary','remarks']

class MessageForm(forms.ModelForm):
    message=forms.CharField(widget=forms.HiddenInput())


    class Meta:
        model=Message
        fields=['message']