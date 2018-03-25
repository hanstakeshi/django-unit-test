from django.db import models
from filebrowser.fields import FileBrowseField
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
# Create your models here.

class ModelExample(models.Model):

    img_example = FileBrowseField('Imagen Label',
                                max_length=200, blank=True,
                                extensions=['.jpg', '.png', '.gif'],
                                directory='img_example')

    rich_example = RichTextField("Example", blank=True)

    class Meta:
        verbose_name = "Model Exmaple"
        verbose_name_plural = "Model Examples"

    def __unicode__(self):
        return u"Model Example"


class Autor(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('web:autor_detalle', kwargs={'id': self.id})

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
