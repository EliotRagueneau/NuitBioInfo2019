from django.shortcuts import render
from django.views.generic import ListView
from .models import Rubric, Topic, Article


class RubricList(ListView):
    model = Rubric
    context_object_name = "rubrics"
    template_name = "articles/rubric_list.html"


class TopicList(ListView):
    model = Topic
    context_object_name = "topics"
    template_name = "articles/topic_list.html"

    def get_queryset(self):
        return Topic.objects.filter(rubric__name=self.kwargs['rubric_name'])


class ArticleList(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/article_list.html"

    def get_queryset(self):
        return Article.objects.filter(topic__name=self.kwargs['topic_name'])
