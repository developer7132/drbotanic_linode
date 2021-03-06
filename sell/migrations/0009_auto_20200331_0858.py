# Generated by Django 3.0.2 on 2020-03-31 08:58

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0008_term'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('content', djrichtextfield.models.RichTextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Term',
            new_name='Contact',
        ),
        migrations.DeleteModel(
            name='Policy',
        ),
    ]
