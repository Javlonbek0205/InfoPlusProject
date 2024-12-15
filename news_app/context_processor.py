from news_app.models import News


def latest_news(request):
    latest_news = News.objects.filter(status='PT').order_by('-publish_time')[:10]
    context = {
        'latest_news': latest_news,
    }
    return context