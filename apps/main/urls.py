from django.urls import path
from apps.main.views import PageView, index, ContactView


urlpatterns = [
    path('', index, name='index'),
    path('<str:slug>/', PageView.as_view(), name='page'),
    path('<str:slug>/', ContactView.as_view(), name='contact'),
]
