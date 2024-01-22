from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['format_post', 'title_post', 'text_post', 'category', 'author' ]

   def clean(self):
       cleaned_data = super().clean()
       text_post = cleaned_data.get("text_post")
       if text_post is not None and len(text_post) < 20:
           raise ValidationError({
               "text_post": "Текст слишком короткий. Необходимо минимум 20 символов."
           })
       title_post = cleaned_data.get("title_post")
       if title_post == text_post:
           raise ValidationError(
               "Описание не должно быть идентичным названию."
           )

       return cleaned_data