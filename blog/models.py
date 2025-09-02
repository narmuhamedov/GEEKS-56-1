from django.db import models

class Blog(models.Model):
  CATEGORY_BLOG = (
    ('Машины', 'Машины'),
    ('Недвижимость', 'Недвижимость'),
    ('Кино', 'Кино')
  )
  title = models.CharField(max_length=50, verbose_name='укажите название блога')
  images = models.ImageField(upload_to='blog/', verbose_name='загрузите фото')
  description = models.TextField(verbose_name='укажите описание блога')
  link_blog = models.URLField(verbose_name='вставьте доп ссылку на контент')
  category_blog = models.CharField(max_length=100, choices=CATEGORY_BLOG, default='Кино')
  video_url = models.URLField(verbose_name='укажите ссылку с youTube', null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = 'новость'
    verbose_name_plural = 'новости'