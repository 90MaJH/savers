##default import
from django.db import models

##imageTest import
from django.urls import reverse



# Create your models here.



##User Models



##Test Models
class Post(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return self.title



class imageTest(models.Model):
    image = models.ImageField(upload_to='%Y/%m/%d/orig', null=True)
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered', null=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        url = reverse('detail', kwargs={'pk': self.pk})
        return url


