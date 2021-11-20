from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

def dateAdd():
    date = str(datetime.today())
    return date


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    STATUS = (('Publish', 'Publish'), ('Private', 'Private'),) 

    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, blank=True, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS, blank=True, null=True)
    category = models.ManyToManyField(Category)
    
    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()

