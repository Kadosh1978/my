from django.urls import path

from news.views import CategoryListView
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostDelete, find, PostSearch, PostCreate, PostUpdate, subscribe


urlpatterns = [

   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='find'),
   path('post/create/', PostCreate.as_view(), name='post_create'),
   path('post/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_update'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
   path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
]