from django.urls import path
from scanner.views import spider,ajaxspider
urlpatterns = [
    path('spider/', spider),
    path('ajaxspider/', ajaxspider),
]
