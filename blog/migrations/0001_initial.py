# Generated by Django 2.2.9 on 2020-01-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Öğrenci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('soyisim', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('doğum_tarihi', models.DateField()),
                ('okul', models.CharField(max_length=50)),
                ('bölüm', models.CharField(max_length=50)),
                ('sınıf', models.CharField(choices=[('1', '1. Sınıf'), ('2', '2. Sınıf'), ('3', '3. Sınıf'), ('4', '4. Sınıf')], max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]