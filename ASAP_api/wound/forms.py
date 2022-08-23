from django import forms
form .models import BurnPic

class BurnPicUploadForm(forms.ModelForm):
    class Meta:
        model = BurnPic
        fields = ['photo']