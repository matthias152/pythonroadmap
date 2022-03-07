# Generated by Django 3.2.9 on 2022-03-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_auto_20220307_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-05-21'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
    ]