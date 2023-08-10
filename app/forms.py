from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import SendAppointment, Contact, Comment


class SendAppointmentForm(forms.ModelForm):
    class Meta:
        model = SendAppointment
        fields = ('fullname', 'email', 'phone', 'message')
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'cols': '0', 'rows': '5'}),

        }


class SignUpForm(UserCreationForm):
    phone = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('username', 'phone', 'password1', 'password2')


class ContactForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForms, self).__init__(*args, **kwargs)
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'
            f.widget.attrs['placeholder'] = fname

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'message':forms.Textarea(attrs={
                'col':'7',
                'rows':'9'
            })
        }


class CommentForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(CommentForm,self).__init__(*args,**kwargs)
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'
            f.widget.attrs['placeholder'] = fname
    class Meta:
        model = Comment
        fields = ('name','email','title','message')
