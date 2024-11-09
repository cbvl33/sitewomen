from django.urls import path, re_path, register_converter
from .views import index, categories, categories_by_slug, archive
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', index),
    path('cats/<int:cat_id>/', categories),
    path('cats/<slug:cat_slug>/', categories_by_slug),
    path('archive/<year4:year>/', archive),
]