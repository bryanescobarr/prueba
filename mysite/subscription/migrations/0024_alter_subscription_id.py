# Generated by Django 3.2.2 on 2021-05-13 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0023_subscription_subscriber_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
