# coding: utf-8
from django.db import models
import datetime
from django.utils import timezone

class TypeStatus(object):
	PUBLISH = 'PUB'
	HIDDEN = 'HID'
	DRAFT = 'DRF'
	STATUS_CHOICES = (
		(PUBLISH, 'Опубликовано'),
		(HIDDEN, 'Скрыто'),
		(DRAFT, 'Черновик'),
		)

class CategoriesArticles(models.Model):
	status = models.CharField(max_length=3,
                              choices=TypeStatus.STATUS_CHOICES,
                              default=TypeStatus.PUBLISH,
                              verbose_name="Статус публикации",)
	order = models.IntegerField(verbose_name="Сортировка", help_text="Только числа",default=0)
	name = models.CharField(max_length=200, verbose_name="Имя категории")
	short_description = models.CharField(max_length=200,
										 verbose_name="Краткое описание категории",
										 help_text="Не более 200 символов",)
	description = models.TextField(verbose_name="Описание категории",)
	last_modified = models.DateTimeField(auto_now=True)
	slug = models.SlugField()

	def __unicode__(self):
		return self.name


class TagArticles(models.Model):
	name = models.CharField(max_length=200,
							verbose_name="Тег",
							)
	slug = models.SlugField()

	def __unicode__(self):
		return self.name

class Articles(models.Model):
	category_id = models.ForeignKey(CategoriesArticles, verbose_name="Категория")
	tagList = models.ManyToManyField(TagArticles, verbose_name="Теги")
	slug = models.SlugField()
	date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
	last_modified = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")
	date_publish = models.DateTimeField(verbose_name="Дата публикации")
	status = models.CharField(max_length=3,
                              choices=TypeStatus.STATUS_CHOICES,
                              default=TypeStatus.PUBLISH,
                              verbose_name="Статус публикации",)
	title = models.CharField(max_length=200, verbose_name="Название статьи")
	short_description = models.CharField(max_length=200,
											verbose_name="Краткое описание",
											help_text="Не более 200 символов",)
	content = models.TextField(verbose_name="Контент")

	def __unicode__(self):
		return self.title	
