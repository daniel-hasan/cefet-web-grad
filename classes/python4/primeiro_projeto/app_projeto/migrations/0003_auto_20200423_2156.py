# Generated by Django 3.0.5 on 2020-04-23 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projeto', '0002_tesouro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='autores',
        ),
        migrations.RemoveField(
            model_name='post',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Tesouro',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
