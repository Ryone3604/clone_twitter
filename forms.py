from django import forms
from .models import Post, ProSetting

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ("content","photo")
        labels={
           'content':'',
           'photo':'画像'
           }
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': "what's happening?", 
            'cols': '60', 'rows': '10',
            'border' : '0',
        })}

class ProSettingForm(forms.ModelForm):

    class Meta():
        
        model = ProSetting
        fields = ("headphoto","prophoto","content")
        labels={
           'content':'自己紹介',
           'headphoto':'ヘッダー画像',
           'prophoto':'プロフィール画像',
           }
        widgets = {
            'content': forms.Textarea(attrs={ 
            'cols': '50', 'rows': '10',
            
        })}

        

        
        