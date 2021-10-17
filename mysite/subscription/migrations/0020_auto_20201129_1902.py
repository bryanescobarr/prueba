# Generated by Django 3.1.1 on 2020-11-29 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0019_subscription_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='format',
            field=models.CharField(choices=[('pdf', 'PDF'), ('print', 'Print'), ('print_and_pdf', 'Print and PDF')], default='pdf', max_length=255),
        ),
    ]
