from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify  # для фильтрации

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

# Create your views here.
def index(request):
    '''
    t = render_to_string('women/index.html')
    return HttpResponse(t)🥰
    '''
    data = {'title':'главная страница?',
            'menu':menu,
            'float': 28.56,
            'lst': [1, 2, 3, 'abc'],
            'set': {1, 2, 3},
            'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
            'obj': MyClass(10, 20),
            'url': slugify('the main PAGE')}
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title':'О сайте'})


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')

def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('sport', ))
        return redirect(uri)
    
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



