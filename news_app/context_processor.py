from news_app.models import News, Category


def latest_news(request):
    latest_news = News.objects.filter(status='PT').order_by('-publish_time')[:10]
    categories = Category.objects.all()
    context = {
        'latest_news': latest_news,
        'categories': categories
    }
    return context