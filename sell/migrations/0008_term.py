# Generated by Django 3.0.2 on 2020-01-27 11:47

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0007_policy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', djrichtextfield.models.RichTextField()),
            ],
        ),
    ]