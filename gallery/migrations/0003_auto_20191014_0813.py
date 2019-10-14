# Generated by Django 2.2.5 on 2019-10-14 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20191014_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='作品标题', max_length=50),
        ),
    ]