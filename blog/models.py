from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField('カテゴリ名',max_length=12)
    create_at = models.DateTimeField("作成日",default=timezone.now)
    def __str__(self):
        return self.name
    
class FreePoster(models.Model):
    poster_name = models.CharField('ユーザー名',max_length=16)
    password = models.CharField('パスワード',max_length=8)
    email = models.EmailField('メールアドレス')
    create_at = models.DateTimeField('加入日',default=timezone.now)
    
    def __str__(self):
        return self.poster_name 
    
class Post(models.Model):
    owner = models.ForeignKey(FreePoster,verbose_name="投稿者",on_delete=models.PROTECT)
    category = models.ForeignKey(Category, verbose_name="カテゴリー", on_delete=models.PROTECT)
    title = models.TextField('キャッチコピー', max_length=12, default="キャッチコピーの文章です。12文字まで")
    pre_text = models.TextField('タイトル',max_length=100, default="本来のタイトルです。100文字まで。")
    text = models.TextField("本文", max_length=2000, default="本文")
    images = models.ImageField(upload_to="", null=True) 
    create_at = models.DateTimeField("作成日", default=timezone.now)
    
    def __str__(self):
        return self.title[:20] + "　カテゴリ：" +  str(self.category) + "　BY：" + str(self.owner)
    
    
class Comment(models.Model):
    name = models.CharField('お名前', max_length=16,null=True)
    text_comment = models.TextField("本文",max_length=200)
    post = models.ForeignKey(Post, verbose_name="関連コメント",on_delete=models.CASCADE)
    create_at = models.DateTimeField("作成日", default=timezone.now)
    
    def __str__(self):
        return self.text_comment + "　by:" + self.name
    
class StablePage(models.Model):
    owner = models.ForeignKey(FreePoster,verbose_name="投稿者",on_delete=models.PROTECT)
    pre_text = models.TextField('タイトル',max_length=100, default="本来のタイトルです。100文字まで。")
    text = models.TextField("本文", max_length=2000, default="本文")
    images = models.ImageField(upload_to="", null=True) 
    create_at = models.DateTimeField("作成日", default=timezone.now)
    
    def __str__(self):
        return self.pre_text
        