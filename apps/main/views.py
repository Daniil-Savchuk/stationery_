from django.shortcuts import render
from django.views import generic

from apps.main.models import Page, Contact


def index(request):
    return render(request, 'index.html')


class PageView(generic.DetailView):
    model = Page
    template_name = 'main/page.html'
    queryset = Page.objects.all()

class ContactView(generic.DetailView):
    model = Contact
    template_name = 'main/contact.html'
    queryset = Contact.objects.all()
