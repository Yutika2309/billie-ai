# Generated by Django 5.0.6 on 2024-05-30 15:37

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
                ('query_text', models.TextField()),
                ('chat_response', models.CharField(max_length=500)),
            ],
        ),
    ]
