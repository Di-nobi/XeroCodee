from .views import login, callback, get_repos
from django.urls import path

urlpatterns= [
    path('', login, name='login'),
    path('', callback, name='callback'),
    path('', get_repos, name='get_repos')
]