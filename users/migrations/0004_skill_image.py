# Generated by Django 3.2.7 on 2022-07-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profiles_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='skills/'),
        ),
    ]