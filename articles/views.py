from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

from . import models


class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'article_detail.html'


class ArticleUpdateView(UpdateView):
    model = models.Article
    fields = ['title', 'body']
    template_name = 'article_update.html'


class ArticleDeleteView(DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
