# Generated by Django 4.1 on 2022-08-09 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('figma', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stories',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='stories',
            old_name='text',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='stories',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stories_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stories',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='stories',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='stories',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AddField(
            model_name='stories',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
