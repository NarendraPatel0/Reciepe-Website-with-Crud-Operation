# Generated by Django 5.0 on 2024-01-02 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insertvalue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
    ]
