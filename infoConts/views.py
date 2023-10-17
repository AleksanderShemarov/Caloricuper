# from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView
from .models import LastInfo, Developer

# Create your views here.


class NewInfoView(TemplateView):

    template_name = "info.html"


class LastNewsContsView(ListView):
    template_name = "info.html"
    model = LastInfo
    context_object_name = "last_info"
    ordering = ["-date"]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['devs'] = Developer.objects.all()
        return context
