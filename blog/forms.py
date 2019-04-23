from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):
    
    class Meta:
            model = Comment
            fields = ('name','text_comment')
            widgets = {
                    "text_comment": forms.TextInput(attrs={"class":"form-control"})
                    }