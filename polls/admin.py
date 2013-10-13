from django.contrib import admin
from polls.models import Polls, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question']
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
		

admin.site.register(Polls, PollAdmin)