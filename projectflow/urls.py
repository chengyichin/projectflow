from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^edit/$', views.edit_docs),
    url(r'', include('blog.urls')),
]
