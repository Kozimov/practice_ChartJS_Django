# Generated by Django 4.0 on 2022-03-27 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_mazmuni'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Postlar'},
        ),
        migrations.AddField(
            model_name='post',
            name='ovozlarSoni',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
