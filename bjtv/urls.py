"""bjtv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from local import views as myviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', myviews.register, name='register'),
    url(r'^register/', myviews.register, name='register'),
    url(r'^login/', myviews.login, name='login'),
    url(r'^add_url/', myviews.add_url, name='add_url'),
    url(r'^get_url_detail/', myviews.get_url_detail, name='get_url_detail'),
]
