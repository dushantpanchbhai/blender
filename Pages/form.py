from django import forms 
from .models import *
from django.forms import ModelForm

class ModelsForm(ModelForm):
    class Meta:
        model = Models
        fields = ['title','link','img'] 
        widgets = {'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name of model'}),
        'link': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter link'}),
        'img':forms.FileInput(attrs={'class': 'form-control'})}
        
class VideosForm(ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title','url']
        labels = {
            'url':'URL  (https://www.youtube.com/embed/..)'
        }
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'url':forms.TextInput(attrs={'class':'form-control','placeholder':'https://www.youtube.com/embed/.....'})}

CHOICES = [
        (0, '-----'),
        (1, 'very bad'),
        (2, 'bad'),
        (3, 'fine'),
        (4, 'good'),
        (5, 'excellent')
]


# class FeedbackForm(ModelForm):
#     class Meta:
#         model = Feedback
#         fields = "__all__"
#         widgets = {'email':forms.TextInput(attrs={'class':'form-control'}),
#         'website_rating':forms.Select(attrs={'class':'form-control'}),
#         'artwork_rating':forms.Select(attrs={'class':'form-control'}),
#         'youtube_rating':forms.Select(attrs={'class':'form-control'}),
#         'feedback':forms.Textarea(attrs={'class':'form-control'})}
        
class GeeksForm(forms.Form):
    email = forms.EmailField(required=True)
    website_rating = forms.ChoiceField(required=True,choices = CHOICES,widget=forms.Select(attrs={'class':'form-control'} )) 
    artwork_rating = forms.ChoiceField(required=True,choices = CHOICES) 
    youtube_rating = forms.ChoiceField(required=True,choices = CHOICES)
    feedback = forms.CharField(required=True,max_length=200,widget=forms.Textarea(attrs={'row':'5'}))
    email.widget.attrs.update({'class': 'form-control','placeholder':'enter your email','id':"inputEmail3"})
    website_rating.widget.attrs.update({'class': 'form-control','type':'checklist'})
    artwork_rating.widget.attrs.update({'class': 'form-control','id':"inputState"})
    youtube_rating.widget.attrs.update({'class': 'form-control'})
    feedback.widget.attrs.update({'class': 'form-control','placeholder':'What more can be improved?'})