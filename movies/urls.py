from django.urls import path
from .views import MoviesListView,MoviesDetailView
urlpatterns = [
   path('', MoviesListView.as_view(), name='movies_list'),
   path('<int:pk>', MoviesDetailView.as_view(),name='movies_detail')
]
