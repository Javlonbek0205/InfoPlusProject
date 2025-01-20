from django.urls import path
from news_app.views import contact_form_view, \
    get_404, NewsDetailView, news_category_view, NewsUpdateView, \
    NewsDeleteView, NewsCreateView, admin_page_view, SearchListView

urlpatterns=[
    path('single_page/<slug:slug>/', NewsDetailView.as_view(), name='single_page'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('<slug:slug>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('<slug:slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('search/', SearchListView.as_view(), name='news_search'),
    path('adminpage/', admin_page_view, name='admin_page'),
    path('contact_form/', contact_form_view, name='contact_form' ),
    path('get_404/', get_404, name='get_404'),
    path('<str:category>/', news_category_view, name='news_category'),
]