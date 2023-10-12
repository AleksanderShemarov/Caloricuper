# from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import LastInfo

# Create your views here.


class NewInfoView(TemplateView):

    template_name = "info.html"


class LastNewsView(ListView):
    model = LastInfo
    context_object_name = "last_info"
    template_name = "info.html"
    ordering = ["-date"]
