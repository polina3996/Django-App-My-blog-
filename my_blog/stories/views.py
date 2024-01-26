from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import Stories

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Написать историю", 'url_name': 'add_story'},
]


# Create your views here.
def about(request):
    """A view that displays about-page"""
    return render(request, 'stories/about.html', context={})


def addstory(request):
    """A view that displays a form to add a story"""
    return render(request, 'stories/addstory.html', context={})


def index(request):
    """A view that displays main page with all stories"""
    return render(request, 'stories/index.html', context={})


def story(request, story_slug: str):
    """A view that displays a certain story with the possibility to edit it"""
    QS = get_object_or_404(Stories, slug=story_slug)
    return render(request, 'stories/story.html', context={'queryset': QS})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
