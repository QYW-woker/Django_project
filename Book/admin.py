from django.contrib import admin

# Register your models here.
from Book.models import BookInfo, PeopleInfo
# 注册模型类,重新运行
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
