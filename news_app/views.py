from urllib import request
from urllib.request import HTTPRedirectHandler

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView
from hitcount.views import HitCountDetailView

from .custom_permission import UserLoggedAdmin
from .forms import ContactForm, CommentForm
from .models import Category, News, Comment


# Create your views here.
def home_view(request):
    categories = Category.objects.all()
    news = News.objects.filter(status='PT').order_by('-publish_time')[:5]
    abroad_one = News.objects.filter(status='PT', category__name__in=['Jahon', 'World', 'Мир']).order_by('-publish_time')[0]
    abroad_news = News.objects.filter(status='PT', category__name__in=['Jahon', 'World', 'Мир']).order_by('-publish_time')[1:6]
    sport_one = News.objects.filter(status='PT', category__name__in=['Sport', 'Sport', 'Спорт']).order_by('-publish_time')[0]
    sport_news = News.objects.filter(status='PT', category__name__in=['Sport', 'Sport', 'Спорт']).order_by('-publish_time')[1:6]
    techno_one = News.objects.filter(status='PT', category__name__in=['Texnologiya', 'Technology', 'Технологии']).order_by('-publish_time')[0]
    techno_news = News.objects.filter(status='PT', category__name__in=['Texnologiya', 'Technology', 'Технологии']).order_by('-publish_time')[1:6]
    local_one = News.objects.filter(status='PT', category__name__in=['Mahalliy', 'Local', 'Местный']).order_by('-publish_time')[0]
    local_news = News.objects.filter(status='PT', category__name__in=['Mahalliy', 'Local', 'Местный']).order_by('-publish_time')[1:6]
    context = {'categories': categories,
               'news': news,
               'abroad_one': abroad_one,
               'abroad_news': abroad_news,
               'sport_one': sport_one,
               'sport_news': sport_news,
               'techno_one': techno_one,
               'techno_news': techno_news,
               'local_one': local_one,
               'local_news': local_news,
               }
    return render(request, 'index.html', context)

class NewsDetailView(HitCountDetailView):
    model = News
    count_hit = True
    form_class  = CommentForm
    template_name = 'single_page.html'
    context_object_name = 'article'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news'] = News.objects.filter(status='PT').order_by('-publish_time')[:4]
        context['article'] = self.object
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['comment_count'] = self.object.comments.count()
        return context
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            news = self.get_object()
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_form = comment_form.save(commit=False)
                comment_form.user = request.user
                comment_form.news = news
                comment_form.save()
                return redirect('single_page', slug=news.slug)
            else:
                return redirect('single_page', slug=news.slug)
        else:
            return redirect('login')
def contact_form_view(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        contact_form_url = reverse('contact_form')  # 'contact_form' nomli URLni olish
        return HttpResponse(f'<h1>Sizning habaringiz jo\'natildi! <a href="{contact_form_url}">Ortga</a></h1>')
    context = {'form': form}
    return render(request, 'contact.html', context)

def get_404(request):
    return render(request, '404.html')

def news_category_view(request, category):
    news = News.objects.filter(category__name=category)
    context = {'news': news}
    return render(request, 'category_news_list.html', context)

class NewsDeleteView(UserLoggedAdmin,DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home')

class NewsUpdateView(UserLoggedAdmin,UpdateView):
    model = News
    fields = ['title','title_uz','title_ru','title_en', 'category', 'status','body','body_uz','body_ru','body_en', 'image',]
    template_name = 'crud/news_update.html'
    def get_success_url(self):
        return reverse_lazy('single_page', kwargs={'slug': self.object.slug})


class NewsCreateView(UserLoggedAdmin,CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ['title','title_uz','title_ru','title_en', 'category', 'status','body','body_uz','body_ru','body_en', 'image',]
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.slug  = slugify(form.instance.title)
        return super().form_valid(form)

@login_required
@user_passes_test(lambda u:u.is_superuser)
def admin_page_view(request):
    admin_users = User.objects.filter(is_superuser=True)
    news = News.objects.all()
    context = {
        'admin_users': admin_users,
        'news': news
    }
    return render(request, 'pages/admin_page.html', context)

class SearchListView(ListView):
    model = News
    template_name = 'search_result.html'
    context_object_name = 'news'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )