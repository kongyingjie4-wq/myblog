from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)        # 文章标题
    content = models.TextField()                     # 文章正文
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间
    views = models.IntegerField(default=0)           # 阅读量

    def __str__(self):
        return self.title