from django.urls import path,include
from . import views
from rest_framework import routers

app_name='library'

router=routers.DefaultRouter()

router.register('books', views.BookViewSet,)
router.register('genres', views.GenreViewSet,)
router.register('quotes', views.QuoteViewSet,)

urlpatterns	= [

    path('books/', views.BookListView.as_view(), name='book_list'),
    path('book/<pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('quotes/', views.QuoteListView.as_view(), name='quote_list'),
    path('quote/<pk>/', views.QuoteDetailView.as_view(), name='quote_detail'),

    path('genre/<pk>/', views.GenreDetailView.as_view(), name='genre_list'),
    path('', include(router.urls)),
    ]