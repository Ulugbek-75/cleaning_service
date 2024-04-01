from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
import string
import random


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Category title'))
    slug = models.SlugField(max_length=255, verbose_name='Category slug',
                            unique=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Servis(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='servis', null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    text = models.TextField()
    main_image = models.ImageField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    count = models.PositiveIntegerField()

    @staticmethod
    def __generate_slug(slug):
        data = string.ascii_lowercase
        random_data = "".join([data[random.randint(0, len(data) - 1)] for i in range(6)])
        return slug + random_data

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if Servis.objects.filter(slug=self.slug).exists():
            self.slug = self.__generate_slug(self.slug)
        super(Servis, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



