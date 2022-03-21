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
    place = models.ForeignKey(Place, on_delete=models.PROTECT)
    site_section = models.ForeignKey('SiteSection', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id}-{self.place.name}'

    class Meta:
        ordering = ('id',)


class PostSection(models.Model):
    content = models.CharField(max_length=5000)
    index = models.PositiveSmallIntegerField()
    content_type = models.ForeignKey('PostSectionType', on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        desc = self.content.strip()
        desc = desc[:20] if len(desc) > 20 else desc
        return f'{self.post.place.name}-{self.content_type}: {desc}'

    class Meta:
        verbose_name = "sección"
        verbose_name_plural = "secciones"
        ordering = ('post', 'index')
        constraints = [
            models.UniqueConstraint(
                fields=["index", "post"], name="unique_sectionIndex_post"
            )
        ]


class PostSectionType(models.Model):
    description = models.CharField(max_length=100)
    css_class = models.CharField(max_length=50)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "tipo de sección"
        verbose_name_plural = "tipos de sección"


class SiteSection(models.Model):
    name = models.CharField(max_length=50)
    banner_path = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "sección del sitio"
        verbose_name_plural = "secciones del sitio"
        ordering = ('id',)
