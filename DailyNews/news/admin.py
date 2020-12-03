from django.contrib import admin
from .models import Category, Member, Article,Comment

admin.site.register(Category)
admin.site.register(Member)
admin.site.register(Article)
admin.site.register(Comment)
