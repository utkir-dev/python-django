from django.urls import path
from myapp.views import hello,goodbye, get_products, get_prepearing, get_completed

urlpatterns = [
    path('hello/', hello),
    path('goodbye', goodbye),
    path('all', get_products),
    path('completed', get_completed),
    path('prepearing', get_prepearing),
]
