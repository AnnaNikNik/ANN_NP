from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from .models import *
#from .moels import Post, Category, PostCategory, Author, User
from datetime import datetime, date, time
from django import forms


class PostFilter(FilterSet):
   category = ModelChoiceFilter(
       field_name='postcategory__category',
       queryset=Category.objects.all(),
       label='Категория',
       empty_label='Все категории'
   )
   min_pub_date=DateFilter(
       time_post=forms.DateInput(attrs={'type': 'date'}),
       filed_name='p_date'

   )

   class Meta:
       model = Post
       fields = {
           'title_post': ['icontains'],
           'text_post': ['icontains'],
       }
