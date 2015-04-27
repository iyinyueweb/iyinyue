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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('comment_time', models.DateTimeField(null=True, blank=True, default=datetime.datetime(2015, 4, 26, 15, 2, 47, 161583, tzinfo=utc), verbose_name='comment_time')),
                ('comment_content', models.CharField(max_length=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('state', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('birthday', models.DateField(null=True, blank=True, verbose_name='birthday')),
                ('password', models.CharField(max_length=100)),
                ('sex', models.IntegerField(null=True, blank=True, default=1)),
                ('email', models.EmailField(null=True, max_length=100, blank=True)),
                ('tag', models.CharField(null=True, max_length=200, blank=True)),
                ('head_img', models.CharField(null=True, max_length=100, blank=True)),
                ('register_time', models.DateField(null=True, blank=True, default=datetime.datetime(2015, 4, 26, 15, 2, 47, 150583, tzinfo=utc))),
                ('last_time', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('album', models.CharField(null=True, max_length=100, blank=True)),
                ('year', models.CharField(null=True, max_length=100, blank=True)),
                ('artist', models.CharField(null=True, max_length=100, blank=True)),
                ('comment', models.CharField(null=True, max_length=100, blank=True)),
                ('genre', models.CharField(null=True, max_length=100, blank=True)),
                ('path', models.CharField(null=True, max_length=100, blank=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('music_category', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MusicTag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('tag_time', models.DateField(default=datetime.datetime(2015, 4, 26, 15, 2, 47, 165584, tzinfo=utc), verbose_name='tag_time')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('play_list_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayTime',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('play_time', models.IntegerField(null=True, blank=True, default=0)),
                ('add_date', models.DateTimeField(null=True, blank=True, verbose_name='add_date')),
                ('music', models.ForeignKey(to='user.Music')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecommendHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('latest_recommend_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecommendItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
            field=models.ManyToManyField(null=True, related_name='recommend_item', blank=True, to='user.RecommendItem'),
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
            field=models.ManyToManyField(null=True, related_name='musics', blank=True, to='user.PlayTime'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='music',
            name='category',
            field=models.ManyToManyField(null=True, related_name='category', blank=True, to='user.MusicCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='dislike_songs',
            field=models.ManyToManyField(null=True, related_name='dislike_songs', blank=True, to='user.Music'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='favorite_songs',
            field=models.ManyToManyField(null=True, related_name='favorite_songs', blank=True, to='user.PlayTime'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='friends',
            field=models.ManyToManyField(null=True, related_name='friends', blank=True, to='user.Friend'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='play_list',
            field=models.ManyToManyField(null=True, related_name='play_list', blank=True, to='user.PlayList'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iuser',
            name='play_recorded',
            field=models.ManyToManyField(null=True, related_name='play_recorded', blank=True, to='user.PlayTime'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(null=True, related_name='friend', blank=True, to='user.IUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_music',
            field=models.ForeignKey(null=True, related_name='comment_music', blank=True, to='user.Music'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(null=True, related_name='comment_user', blank=True, to='user.IUser'),
            preserve_default=True,
        ),
    ]
