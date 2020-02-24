from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

class User(AbstractUser):
    is_reader = models.BooleanField(default=False)
    is_writer = models.BooleanField(default=False)

class Genre(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    url_address = models.SlugField(max_length=200, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    picture = models.ImageField(upload_to='images/', height_field='height',
                                width_field='width')
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)

    Overview = models.TextField()
    download = models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url_address = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    my_favorite_book_genre = models.ManyToManyField(Genre,related_name='favorite_book_genre')

    def __str__(self):
        return self.user.username

class Quote(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quotes')
    from_writer = models.CharField(max_length=30)
    from_book = models.CharField(max_length=30)
    Overview = models.TextField(max_length=600)
    url_address = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.url_address = slugify(self.Overview[:20])
        super(Quote, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.Overview