from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm
from .models import Category, News
# Create your views here.
def home_view(request):
    categories = Category.objects.all()
    news = News.objects.filter(status='PT').order_by('-publish_time')[:5]
    abroad_one = News.objects.filter(status='PT', category__name='Jahon').order_by('-publish_time')[0]
    abroad_news = News.objects.filter(status='PT', category__name='Jahon').order_by('-publish_time')[1:6]
    sport_one = News.objects.filter(status='PT', category__name='Sport').order_by('-publish_time')[0]
    sport_news = News.objects.filter(status='PT', category__name='Sport').order_by('-publish_time')[1:6]
    techno_one = News.objects.filter(status='PT',category__name='Texnologiya').order_by('-publish_time')[0]
    techno_news = News.objects.filter(status='PT', category__name='Texnologiya').order_by('-publish_time')[1:6]
    local_one = News.objects.filter(status='PT', category__name='Mahalliy').order_by('-publish_time')[0]
    local_news = News.objects.filter(status='PT', category__name='Mahalliy').order_by('-publish_time')[1:6]
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

def single_page_view(request, pk):
    return render(request, 'single_page.html')

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