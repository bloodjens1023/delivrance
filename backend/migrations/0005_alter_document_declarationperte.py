# Generated by Django 5.0.1 on 2024-04-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_document_actenaissance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='declarationPerte',
            field=models.ImageField(blank=True, upload_to='backend/image/perte'),
        ),
    ]
