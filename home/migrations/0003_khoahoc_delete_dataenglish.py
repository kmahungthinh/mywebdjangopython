# Generated by Django 4.1 on 2022-08-17 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_dataenglish'),
    ]

    operations = [
        migrations.CreateModel(
            name='khoaHoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='DataEnglish',
        ),
    ]