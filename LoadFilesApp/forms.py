from django import forms

from .models import Book

# class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    # file = forms.FileField()
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf')