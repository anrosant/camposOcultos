from django.conf.urls import url, include
from django.contrib import admin
from camposApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^camposApp/', include('camposApp.urls')),
]
