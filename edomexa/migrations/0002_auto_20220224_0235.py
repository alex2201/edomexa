# Generated by Django 3.2.12 on 2022-02-24 08:35
from collections import namedtuple

from django.db import migrations


def init_post_section_types(apps, schema_editor):
    SectionType = namedtuple('SectionType', 'description css_class')
    section_types = (
        SectionType('title', 'post-section-type-title'),
        SectionType('subtitle', 'post-section-type-subtitle'),
        SectionType('text', 'post-section-type-text'),
        SectionType('image', 'post-section-type-image'),
    )
    PostSectionType = apps.get_model('edomexa', 'PostSectionType')

    for section_type in section_types:
        new_section_type = PostSectionType(description=section_type.description, css_class=section_type.css_class)
        new_section_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('edomexa', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_post_section_types)
    ]