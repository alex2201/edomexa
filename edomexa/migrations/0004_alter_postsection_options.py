# Generated by Django 3.2.12 on 2022-02-24 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edomexa', '0003_auto_20220224_0346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postsection',
            options={'ordering': ('post', 'index'), 'verbose_name': 'sección', 'verbose_name_plural': 'secciones'},
        ),
    ]
