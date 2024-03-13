from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Post

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'head': ['icontains'],
           'author': ['exact'],
           # количество товаров должно быть больше или равно
        #    'quantity': ['gt'],
           'time_in': [
        #        'lt',  # цена должна быть меньше или равна указанной
               'gt',  # цена должна быть больше или равна указанной
           ],
       }
date = DateFilter(
    field_name='time_in',
    lookup_expr='gt',
    label='Date',
    widget=DateInput(
    attrs={'type': 'date'},
            ),
            )