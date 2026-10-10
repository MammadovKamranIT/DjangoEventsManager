from django.db import models
from django.conf import settings
# from EventProject import settings

# Create your models here.


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # your custom fields here
    pass



class Category(models.Model):
    name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(max_length=100, unique = True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name



class Tag(models.Model):
        name = models.CharField(max_length=100, unique = True)
        class Meta:
            verbose_name = 'Tag'
            verbose_name_plural = 'Tag'
            ordering = ['name']

        def __str__(self):
            return self.name

    



class Event(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    category = models.ForeignKey(
    Category,
    on_delete=models.PROTECT,
    related_name = 'events',)


    tags = models.ManyToManyField(

    Tag,
    related_name = 'events',
            
    )

    author = models.ForeignKey(

        settings.AUTH_USER_MODEL ,
        on_delete = models.CASCADE,
        related_name='events',
            
          
     )


    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
