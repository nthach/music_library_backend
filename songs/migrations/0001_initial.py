# Generated by Django 4.1.1 on 2022-09-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('album', models.IntegerField()),
                ('release', models.DateField()),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
    ]