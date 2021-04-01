# Generated by Django 2.2.3 on 2021-04-01 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_remove_post_modified'),
        ('favourite', '0002_auto_20210401_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
        ),
    ]
