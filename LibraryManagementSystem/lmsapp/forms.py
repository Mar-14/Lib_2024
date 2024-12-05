from django import forms
from .models import  User,Book
from django.core.exceptions import ValidationError

#form.py file dedicted for creating forms
class MyLoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder':'Enter username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class':'form-control',
                   'placeholder':'Enter Password'}
        )
    )


class UserRegisterationForm(forms.ModelForm):
    password=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','first_name','email','password')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
           raise forms.ValidationError('password does not match')
        return cd['password2']
    

class BookAddForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=('title','author','genre','category','price','available_copies','book_image')

    def clean_title(self):
        title=self.cleaned_data.get('title') 
        if not title:
            raise ValidationError("this field is required")
        if len(title)<0:
            raise ValidationError('Post title must be atleast 5 character long')
        return title
    def clean_book_image(self):
        book_image=self.cleaned_data.get('book_image')
        if book_image:
            extensions=['png','jpg','jpeg']
            image_extension=book_image.name.lower().split('.')[-1]
            if image_extension not in extensions:
                raise ValidationError('Image must be in jpg,png or jpeg')
            return book_image