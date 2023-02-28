from django.shortcuts import render
from django.views import generic

from apps.main.models import Page, Contact, ProductSet


def index(request):
    page = Page.objects.get(slug='home')
    product_sets = ProductSet.objects.filter(is_active=True)
    return render(request, 'index.html', {'page': page, 'product_sets': product_sets})


class PageView(generic.DetailView):
    model = Page
    template_name = 'main/page.html'
    queryset = Page.objects.all()

class ContactView(generic.DetailView):
    model = Contact
    template_name = 'main/contact.html'
    queryset = Contact.objects.all()
