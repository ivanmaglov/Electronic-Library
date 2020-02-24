from django.urls import path,include
from .library_views import home,allbooks,BookDetailViewForAll,allquotes, SearchResultsView
from .reader_views import UpdateMyFavoriteBookGenres,QuoteCreateView,QuateListView,QuateListUpdate,QuateDelete, QuoteDetailView
from .writer_views import BookCreateView,BookListView,BookDetailView,BookUpdateView,BookDeleteView


urlpatterns = [
                                  path('', home, name='home'),
                                  path('allbooks/', allbooks , name='all_books'),
                                  path('allquotes/', allquotes , name='all_quotes'),
    path('search/', SearchResultsView.as_view(), name='book_search_list_view'),
                                  path('book/<slug:url_address>/',BookDetailViewForAll.as_view(),name='book_detail_all'),

    path('readers/', include(([
                                  path('', allbooks , name='readerhome'),
                                  path('add_quote/', QuoteCreateView.as_view(), name='add_quote'),
                                  path('genres/<int:pk>/',  UpdateMyFavoriteBookGenres.as_view() , name='genres'),
                                  path('quote_list/', QuateListView.as_view(), name='quote_list'),
                                  path('quote_edit/<int:pk>/', QuateListUpdate.as_view(), name='quote_update'),
                                  path('quote/<int:pk>/delete', QuateDelete.as_view(), name='quote_delete'),
                                  path('quote/<slug:url_address>/',QuoteDetailView.as_view(),name='quote_detail'),
                              ], 'library'), namespace='readers')),

    path('writers/', include(([
                                 path('add_book/', BookCreateView.as_view(), name='add_book'),
                                 path('book_list/', BookListView.as_view(), name='book_list'),
                                 path('', allbooks, name='writerhome'),
                                 path('book/<slug:url_address>/',BookDetailView.as_view(),name='book_detail'),
                                 path('book_edit/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
                                 path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
                              ], 'library'), namespace='writers')),

]
