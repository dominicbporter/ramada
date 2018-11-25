from django.urls import path
from web.views import index, auckland

urlpatterns = [
    path('', index.index_view, name='index'),
    path('auckland/', auckland.auckland_view, name='auckland')
]