# Generated by Django 3.1 on 2020-09-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuesday', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_User',
            fields=[
                ('adminuser_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('password', models.CharField(max_length=70)),
            ],
        ),
    ]