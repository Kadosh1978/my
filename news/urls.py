from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, ProductDelete, find, PostSearch, PostCreate, ProductUpdate


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='find'),
   path('create/', PostCreate.as_view(), name='create'),
   path('<int:pk>/edit/', ProductUpdate.as_view(), name='update'),
   path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'), 
]