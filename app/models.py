from django.db import models

class Profile(models.Model):
    # フォーム・データベースが空でもOKの場合、null=True, blank=Trueを設定する
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    job = models.TextField('仕事')
    introduce = models.TextField('自己紹介')
    github= models.CharField('github', max_length=100, null=True, blank=True)
    twitter= models.CharField('twitter', max_length=100, null=True, blank=True)
    linkedin= models.CharField('linkedin', max_length=100, null=True, blank=True)
    facebook= models.CharField('facebook', max_length=100, null=True, blank=True)
    instagram= models.CharField('instagram', max_length=100, null=True, blank=True)
    topimage= models.ImageField(upload_to='images', verbose_name='トップ画像')
    subimage= models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name

class Works(models.Model):
    # フォーム・データベースが空でもOKの場合、null=True, blank=Trueを設定する
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    images = models.ImageField(upload_to= 'images', verbose_name='イメージ画像')
    thmbnail = models.ImageField(upload_to= 'images', verbose_name='サムネイル', null=True, blank=True)
    skill= models.CharField('',

