# Generated by Django 3.1.1 on 2020-09-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='Images/Upload')),
                ('date', models.CharField(max_length=70)),
                ('time', models.TimeField()),
                ('position', models.CharField(max_length=70)),
            ],
        ),
    ]
