from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

from . import models


class ArticleCreateView(CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
