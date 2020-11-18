# Generated by Django 3.1 on 2020-11-13 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='カテゴリ名')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='イベント名')),
                ('max_participant', models.IntegerField(default=0, verbose_name='最大参加者数')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enkai.category', verbose_name='カテゴリ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='主催者')),
            ],
        ),
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enkai.event', verbose_name='イベント')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='参加者')),
            ],
        ),
    ]