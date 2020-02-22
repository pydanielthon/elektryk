"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, login, cart, customer, empty, register, payment, shipping, categories, products
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^cart/$', cart, name='cart'),
    url(r'^customer/$', customer, name='customer'),
    url(r'^empty/$', empty, name='empty'),
    url(r'^payment/$', payment, name='payment'),
    url(r'^register/$', register, name='register'),
    url(r'^shipping/$', shipping, name='shipping'),
    url(r'^categories/$', categories, name='categories'),
    url(r'^products/$', products, name='products'),
]
