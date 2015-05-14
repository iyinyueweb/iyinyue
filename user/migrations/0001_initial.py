# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('comment_time', models.DateTimeField(verbose_name='comment_time', null=True, blank=True, default=datetime.datetime(2015, 5, 12, 0, 36, 13, 30011, tzinfo=utc))),
                ('comment_content', models.CharField(max_length=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('state', models.BooleanField(default=False)),
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
                ('birthday', models.DateField(verbose_name='birthday', null=True, blank=True)),
                ('password', models.CharField(max_length=100)),
                ('sex', models.IntegerField(null=True, blank=True, default=1)),
                ('email', models.EmailField(max_length=100, null=True, blank=True)),
                ('tag', models.CharField(max_length=200, null=True, blank=True)),
                ('head_img', models.CharField(max_length=100, null=True, blank=True)),
                ('register_time', models.DateField(null=True, blank=True, default=datetime.datetime(2015, 5, 12, 0, 36, 13, 20010, tzinfo=utc))),
                ('last_time', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('song_name', models.CharField(max_length=500)),
                ('album', models.CharField(max_length=1000, null=True, blank=True)),
                ('year', models.CharField(max_length=100, null=True, blank=True)),
                ('artist', models.CharField(max_length=500, null=True, blank=True)),
                ('comment', models.CharField(max_length=1000, null=True, blank=True)),
                ('genre', models.CharField(max_length=100, null=True, blank=True)),
                ('path', models.CharField(max_length=1000, null=True, blank=True)),
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
                ('tag_time', models.DateField(verbose_name='tag_time', default=datetime.datetime(2015, 5, 12, 0, 36, 13, 33011, tzinfo=utc))),
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
                ('play_time', models.IntegerField(null=True, blank=True, default=0)),
                ('add_date', models.DateTimeField(verbose_name='add_date', null=True, blank=True)),
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
                ('recommend_date', models.DateTimeField(verbose_name='recommend_date', default=django.utils.timezone.now)),
                ('music', models.ForeignKey(to='user.Music')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recommendhistory',
            name='recommend_items',
            field=models.ManyToManyField(to='user.RecommendItem', related_name='recommend_item', null=True, blank=True),
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
            field=models.ManyToManyField(to='user.PlayTime', related_name='musics', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='music',
            name='category',
            field=models.ManyToManyField(to='user.MusicCategory', related_name='category', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='dislike_songs',
            field=models.ManyToManyField(to='user.Music', related_name='dislike_songs', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='favorite_songs',
            field=models.ManyToManyField(to='user.PlayTime', related_name='favorite_songs', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='friends',
            field=models.ManyToManyField(to='user.Friend', related_name='friends', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='play_list',
            field=models.ManyToManyField(to='user.PlayList', related_name='play_list', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='play_recorded',
            field=models.ManyToManyField(to='user.PlayTime', related_name='play_recorded', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(to='user.IUser', null=True, blank=True, related_name='friend'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_music',
            field=models.ForeignKey(to='user.Music', null=True, blank=True, related_name='comment_music'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(to='user.IUser', null=True, blank=True, related_name='comment_user'),
            preserve_default=True,
        ),
    ]
