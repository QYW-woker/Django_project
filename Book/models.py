from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=32)
    # 重写 str方法以让admin来显示书籍名字
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于那本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
