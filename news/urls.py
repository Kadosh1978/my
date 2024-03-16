from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostDelete, find, PostSearch, PostCreate, PostUpdate


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
   
]