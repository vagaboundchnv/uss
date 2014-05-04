from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    """
    Model for tags of user
    """
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"

class UrlDesc(models.Model):
    """
    Model for Desc of Url
    """
    user = models.ForeignKey(User)
    link = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=64, null=True)        
    tags = models.ManyToManyField(Tag, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Url Descriptions"
