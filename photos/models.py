from django.db import models

class Tag(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Photo(models.Model):
  url_photo = models.URLField(verbose_name='вставьте ссылку картинки')
  created_at = models.DateTimeField(auto_now_add=True)
  tags = models.ManyToManyField(Tag)

  def __str__(self):
    return self.url_photo