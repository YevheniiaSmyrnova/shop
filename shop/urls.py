"""
Main urls module
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^price/', include('price.urls', namespace="price")),
    url(r'^admin/', include(admin.site.urls)),
]

