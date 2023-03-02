from django import forms

class ProductForm(forms.Form):
    title= forms.CharField(max_length=50)
    price= forms.IntegerField()
    description= forms.CharField(widget= forms.Textarea)
    date= forms.DateField()