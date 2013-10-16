#! coding: utf-8

import models

def context(request):
    cats = models.CategoriesArticles.objects.filter()
    context = {
        'cats': {}
    }
    for cat in cats:
        context['cats'][cat.slug] = cat
    print context
    return {'context': context}