from django.urls import path
from .views import home_view, single_page_view, contact_form_view, get_404

urlpatterns=[
    path('', home_view, name='home'),
    path('single_page/<int:pk>/', single_page_view, name='single_page'),
    path('contact_form/', contact_form_view, name='contact_form' ),
    path('get_404/', get_404, name='get_404'),
]