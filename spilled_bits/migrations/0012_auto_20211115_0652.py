# Generated by Django 3.2.9 on 2021-11-14 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spilled_bits', '0011_alter_article_filler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='filler',
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]