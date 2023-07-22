from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import NewInfoView

urlpatterns = [
    path('', NewInfoView.as_view(), name="info"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
