#! coding: utf8
from django.db import models
from django.contrib.auth.models import User
class TypeGenre(object):
	MALE = 'M'
	FEMALE = 'F'
	GENRE = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		)

class Team(models.Model):
	name = models.CharField(max_length=25, unique=True)
	def __unicode__(self):
		return self.name


class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	team = models.ManyToManyField(Team, blank=True, null=True)
	gender = models.CharField(max_length=1,
							choices=TypeGenre.GENRE,
							verbose_name='Пол')
	date_birth = models.DateField(blank=True, null=True)
	slug = models.SlugField(verbose_name='Ссылка на профиль', blank=True, null=True)
	avatar = models.ImageField(verbose_name='Аватар',  upload_to='images/%Y/%m/%d', blank=True, null=True)

	def __unicode__(self):
		return self.user.username