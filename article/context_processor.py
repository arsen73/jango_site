#! coding: utf-8

import models

def context(request):
    cats = models.CategoriesArticles.objects.filter()
    context = {
        'name': {},
        #'href': {}
    }
    for cat in cats:
        #context['href'][cat.slug] = "/article/%s/catigory" % cat.slug
        context['name'][cat.slug] = cat
        #/article/%s/catigory" % self.slug
    return {'cats': context}