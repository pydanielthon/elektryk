from django.urls import path
from django.conf.urls import url
from .views import homepage
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views
urlpatterns = [
     url(r'^$', RedirectView.as_view(url='/')),
     path('', views.homepage, name='homepage')

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)