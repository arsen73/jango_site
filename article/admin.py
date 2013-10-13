# coding: utf-8
from django.contrib import admin
from article.models import CategoriesArticles, TagArticles, Articles

class AdminCategoriesArticles(admin.ModelAdmin):
	list_display = ('name', 'status')

class AdminArticles(admin.ModelAdmin):
	list_display = ('title', 'date_create', 'last_modified', 'status')

admin.site.register(CategoriesArticles, AdminCategoriesArticles)
admin.site.register(TagArticles)
admin.site.register(Articles, AdminArticles)