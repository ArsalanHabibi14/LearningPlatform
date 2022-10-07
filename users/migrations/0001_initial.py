# Generated by Django 3.2.7 on 2022-07-12 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('username', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('user_type', models.CharField(choices=[(1, 'Teacher'), (2, 'Student'), (3, 'Both')], max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='users/')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('website_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('linkdin_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('skills', models.ManyToManyField(to='users.Skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]