# Generated by Django 5.0.6 on 2024-06-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('eleventh', '11th'), ('twelfth', '12th')], max_length=20)),
                ('subject', models.CharField(choices=[('physics', 'Physics'), ('chemistry', 'Chemistry'), ('biology', 'Biology')], max_length=20)),
                ('subject_url', models.URLField(blank=True)),
                ('topic', models.CharField(max_length=50)),
                ('recommended_src', models.CharField(choices=[('creative ideas', 'Ideas'), ('experiments', 'Experiments')], max_length=20)),
                ('chat_response', models.TextField(max_length=200)),
            ],
        ),
    ]
