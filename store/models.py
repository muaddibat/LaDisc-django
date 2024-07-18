from django.db import models
from category.models import Category
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Disc(models.Model):
    artist = models.CharField(_("Artist"), max_length=255)
    album = models.CharField(_("Album"), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    year = models.IntegerField(_("Year"))
    record_label = models.CharField(_("Record Label"), max_length=255)
    code = models.CharField(_("Code"), max_length=255)
    disc_condition = models.CharField(_("Disc Condition"), max_length=255)
    cover_condition = models.CharField(_("Cover Condition"), max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.URLField(_("Image URL"))
    image_url_2 = models.URLField(_("Image URL"), default='null')
    image_url_3 = models.URLField(_("Image URL"), default='null')
    country = models.CharField(_("Country"), max_length=255, default='null')
    style = models.CharField(_("Style"), max_length=255, default='null')
    stock = models.IntegerField(_("Stock"), default=1)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        verbose_name = _('Disc')
        verbose_name_plural = _('Discs')

    def __str__(self):
        return f'{self.artist} - {self.album}'
    
    def get_url(self):
        return reverse('disc_detail', args=[self.category.slug, self.slug])
