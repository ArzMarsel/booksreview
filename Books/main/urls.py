from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='books'),
    path('authors/', views.author1, name='authors'),
    path('<int:pk>', views.More1.as_view(), name='more_book'),
    path('authors/<int:pk>', views.More2.as_view(), name='more_author'),
    path('/date', views.index_date, name='by date'),
    path('/name', views.index_name, name='by name'),
    path('/author', views.index_author, name='by author'),
    path('rate/', views.rate, name='rate'),
    path('review/', views.review, name='review')
]