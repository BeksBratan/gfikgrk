from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return f'{self.title}'


class Comments(models.Model):
    comment_type = models.CharField('Type', max_length=100)
    comment_text = models.TextField('Comment')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.comment_type}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
