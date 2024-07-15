# Generated by Django 4.1 on 2024-07-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasicApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio',
            new_name='portfolio_site',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='picture',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='portfolio_pic',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio_pics'),
        ),
    ]
