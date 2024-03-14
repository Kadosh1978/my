from django.forms import DateInput
from django_filters import FilterSet, DateFilter, ModelChoiceFilter
from .models import Post, Author, User

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):

    author = ModelChoiceFilter(
        field_name= 'author',
        queryset=Author.objects.all(),
        empty_label='Any'


    )
   
    time_in = DateFilter (
          field_name='time_in',
          widget = DateInput(attrs={'type':'date'}),
          label='Date',
          lookup_expr='date__gt'
          

    )

    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
        model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
        fields = {

           # поиск по названию
            'head': ['icontains'],
            # 'author': ['exact'],
           # количество товаров должно быть больше или равно
        #    'quantity': ['gt'],
        #    'time_in': 
        #    [

        #        'gt',  
        #    ],
       }
# date = DateFilter(
#     field_name='time_in',
#     lookup_expr='gt',
#     label='Date',
#     widget=DateInput(
#     attrs={'type': 'date'},
#             ),
#             )