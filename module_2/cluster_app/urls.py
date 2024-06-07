from .views import cluster
from django.urls import path

urlpatterns = [
    path('', cluster, name='cluster')
]