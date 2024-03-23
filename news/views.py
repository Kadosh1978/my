from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from news.forms import PostForm
from .models import Post
from .filters import PostFilter

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'edit.html'

class MyView(PermissionRequiredMixin, View):
    permission_required = ('news.change_post',
                           'news.delete_post',
                           'news.add_post')

    

class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'time_in'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 5



    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = PostFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context

class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'new'

def find(request):
    form = PostForm
    return render(request, 'search.html', {'from': form})

class PostSearch(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)           
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context
    
class PostCreate(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'create.html'

    permission_required = ('news.change_post',
                           'news.delete_post',
                           'news.add_post')

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/articles/create/':
            post.post_type = 'AR'
        return super().form_valid(form)
    

class PostUpdate(LoginRequiredMixin ,UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'

    permission_required = ('news.change_post',
                           'news.delete_post',
                           'news.add_post')

   
    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/articles/<int:pk>/edit/':
            post.post_type = 'AR'
        return super().form_valid(form)


    
class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')

    permission_required = ('news.change_post',
                           'news.delete_post',
                           'news.add_post')

    
    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/articles/<int:pk>/delete/':
            post.post_type = 'AR'
        return super().form_valid(form)