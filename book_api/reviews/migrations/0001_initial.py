# Generated by Django 3.1.2 on 2020-10-03 09:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0002_auto_20201002_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.RegexValidator(message='Must be an integer value between 1 and 5 inclusive.', regex='^([1-5]{1})$')], verbose_name='Book Rating')),
                ('content', models.CharField(max_length=255, verbose_name='Rating Content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date & Time Created')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.book', verbose_name='Book')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ['id'],
            },
        ),
    ]
