from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView

from blogs.models import PostModel
from pages.forms import ContactModelForm
from .models import BannerModel


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['posts'] = PostModel.objects.order_by('-id')[:3]
        data['banners'] = BannerModel.objects.filter(is_active=True)
        return data


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse_lazy('pages:contact')