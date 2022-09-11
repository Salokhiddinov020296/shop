from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class ProductTagModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class BrandModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class SizeModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'


class ColorModel(models.Model):
    code = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class ProductModel(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'))
    short_description = models.CharField(max_length=255, verbose_name=_('short description'))
    long_description = RichTextUploadingField(verbose_name=_('long description'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(verbose_name=_("real price"), default=0)
    sale = models.BooleanField(verbose_name=_('sale'), default=False)
    discount = models.PositiveSmallIntegerField(default=0, verbose_name=_('discount'))
    main_image = models.ImageField(upload_to='products/', verbose_name=_('main_image'))
    category = models.ForeignKey(CategoryModel, related_name='products', on_delete=models.RESTRICT)
    tags = models.ManyToManyField(ProductTagModel, related_name='products', verbose_name=_('tags'))
    sizes = models.ManyToManyField(SizeModel, related_name='products', verbose_name=_('sizes'))
    colors = models.ManyToManyField(ColorModel, related_name='products', verbose_name=_('colors'))
    brand = models.ForeignKey(BrandModel, related_name='products', verbose_name=_('brand'), on_delete=models.RESTRICT,
                              null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def is_discount(self):
        return bool(self.discount)

    def new(self):
        return (timezone.now() - self.created_at).days <= 5

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _('products')