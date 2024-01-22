from django.db import models
from datetime import datetime
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.core.validators import MinValueValidator
from django.urls import reverse



class User(models.Model):
    name = models.CharField(max_length=30)

class Author(models.Model):
    rating_author = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    def update_rating(self):
        posts_rating = Post.objects.filter(author=self).aggregate(pr=Coalesce(Sum('rating_post'), 0))['pr']
        comments_rating = Comment.objects.filter(user=self.user).aggregate(cr=Coalesce(Sum('rating_comm'), 0))['cr']
        posts_comments_rating = Comment.objects.filter(user__author=self).aggregate(pcr=Coalesce(Sum('rating_comm'), 0))['pcr']

        self.rating = posts_rating * 3 + comments_rating + posts_comment_rating
        self.save()


class Category(models.Model):
    name_category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name_category


class Post(models.Model):
    news = 'N'
    article = 'A'
    _format = [
        (news, 'Новость'),
        (article, 'Статья')
    ]

    time_post = models.DateTimeField(auto_now_add=True)
    format_post = models.CharField(max_length=10, choices=_format, default=news)
    title_post = models.CharField(max_length=155, default="Без названия", unique=True)
    text_post = models.TextField(max_length=10000, default="Пусто")
    rating_post = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    liked_post = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory', related_name='posts')

    def __str__(self):
        return f'{self.title_post.title()}: {self.text_post[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


    def like_post(self):
        if self.liked_post:
            return (self.rating_post + 1).int()
        else:
            pass

    def dislike_post(self):
        if self.liked_post:
            return (self.rating_post - 1).int()
        else:
            pass

    def preview(self):
        return self.text_post(124)


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    time_comm = models.DateTimeField(auto_now_add=True)
    text_comm = models.TextField(max_length=455, default="Пусто")
    rating_comm = models.IntegerField(default=0)
    liked_comm = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def like_comm(self):
        if self.liked_comm:
            return (self.rating_comm + 1).int()
        else:
            pass

    def dislike_comm(self):
        if self.liked_comm:
            return (self.rating_comm - 1).int()
        else:
            pass


