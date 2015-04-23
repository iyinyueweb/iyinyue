# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('comment_time', models.DateTimeField(default=datetime.datetime(2015, 4, 23, 9, 13, 34, 402341, tzinfo=utc), blank=True, null=True, verbose_name='comment_time')),
                ('comment_content', models.CharField(max_length=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('password', models.CharField(max_length=100)),
                ('sex', models.IntegerField(default=1, blank=True, null=True)),
                ('email', models.EmailField(max_length=100, blank=True, null=True)),
                ('tag', models.CharField(max_length=200, blank=True, null=True)),
                ('head_img', models.CharField(max_length=100, blank=True, null=True)),
                ('register_time', models.DateField(default=datetime.datetime(2015, 4, 23, 9, 13, 34, 395340, tzinfo=utc), blank=True, null=True)),
                ('last_time', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100, blank=True, null=True)),
                ('year', models.CharField(max_length=100, blank=True, null=True)),
                ('artist', models.CharField(max_length=100, blank=True, null=True)),
                ('comment', models.CharField(max_length=100, blank=True, null=True)),
                ('genre', models.CharField(max_length=100, blank=True, null=True)),
                ('path', models.CharField(max_length=100, blank=True, null=True)),
                ('popular', models.IntegerField(default=0)),
                ('unpopular', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MusicCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('music_category', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MusicTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tag_time', models.DateField(default=datetime.datetime(2015, 4, 23, 9, 13, 34, 406341, tzinfo=utc), verbose_name='tag_time')),
                ('tag_content', models.CharField(max_length=100)),
                ('tag_music', models.ForeignKey(to='user.Music')),
                ('tag_user', models.ForeignKey(to='user.IUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('operation_time', models.DateField(verbose_name='operation_time')),
                ('operation_type', models.CharField(max_length=50)),
                ('operation_music', models.ForeignKey(to='user.Music')),
                ('operation_user', models.ForeignKey(to='user.IUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('play_list_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('play_time', models.IntegerField(default=0, blank=True, null=True)),
                ('add_date', models.DateTimeField(blank=True, null=True, verbose_name='add_date')),
                ('music', models.ForeignKey(to='user.Music')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecommendHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('latest_recommend_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecommendItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('recommend_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='recommend_date')),
                ('music', models.ForeignKey(to='user.Music')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recommendhistory',
            name='recommend_items',
            field=models.ManyToManyField(to='user.RecommendItem', related_name='recommend_item', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recommendhistory',
            name='recommend_user',
            field=models.ForeignKey(to='user.IUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playlist',
            name='play_time',
            field=models.ManyToManyField(to='user.PlayTime', related_name='musics', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='music',
            name='category',
            field=models.ManyToManyField(to='user.MusicCategory', related_name='category', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='dislike_songs',
            field=models.ManyToManyField(to='user.Music', related_name='dislike_songs', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='favorite_songs',
            field=models.ManyToManyField(to='user.PlayTime', related_name='favorite_songs', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='friends',
            field=models.ManyToManyField(to='user.IUser', related_name='friends_rel_+', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='play_list',
            field=models.ManyToManyField(to='user.PlayList', related_name='play_list', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='play_recorded',
            field=models.ManyToManyField(to='user.PlayTime', related_name='play_recorded', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_music',
            field=models.ForeignKey(to='user.Music', blank=True, related_name='comment_music', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(to='user.IUser', blank=True, related_name='comment_user', null=True),
            preserve_default=True,
        ),
    ]
