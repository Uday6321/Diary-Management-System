# Generated by Django 5.1.3 on 2025-01-04 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_demo_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=5000)),
            ],
        ),
    ]
