#! coding: utf-8

import models

def context(request):
    cats = models.CategoriesArticles.objects.all()
    context = {
        'cats': {},
        'tags': {}
    }
    for cat in cats:
    	cat.count = len(models.Articles.objects.filter(category_id=cat.id))
        context['cats'][cat.slug] = cat

    context['tags'] = models.TagArticles.objects.all()
    return {'context': context}