from django.db import models

# Create your models here.
class Library(models.Model):
    title = models.CharField('Title', max_length=50, null=False)
    short_description = models.CharField('Short Description', max_length=150, null=False)
    article_text = models.TextField('Article Text', null=False, blank=False)
    created = models.DateTimeField('Created', auto_now_add=True)
    image = models.ImageField('Image', null=False, blank=False, upload_to="images/")
    video = models.FileField('Video', upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title
