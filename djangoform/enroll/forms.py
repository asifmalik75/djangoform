from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    contact=forms.IntegerField()
    country=forms.CharField()
    city=forms.CharField()
    