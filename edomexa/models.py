from django.db import models


class Town(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "municipio"
        verbose_name_plural = "municipios"

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # Link to google maps location ej: https://goo.gl/maps/e4DiHAEA7PWLsxJc6
    location = models.CharField(max_length=300, blank=True, default='')
    town = models.ForeignKey(Town, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "lugar"
        verbose_name_plural = "lugares"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título post')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo post')
    summary = models.CharField(max_length=250, verbose_name='Resumen post')
    miniature_path = models.CharField(max_length=500, verbose_name='Ruta de miniatura')
    html_path = models.CharField(max_length=500, verbose_name='Ruta de html de post')
    place = models.ForeignKey(Place, on_delete=models.PROTECT)
    site_section = models.ForeignKey('SiteSection', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id}-{self.place.name}'

    class Meta:
        ordering = ('id',)


class SiteSection(models.Model):
    name = models.CharField(max_length=50)
    banner_path = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "sección del sitio"
        verbose_name_plural = "secciones del sitio"
        ordering = ('id',)
