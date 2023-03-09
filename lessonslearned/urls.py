from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from ll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    path('', include('ll.urls')),
    path('', include(('ll.urls', 'search'), namespace='search')),
]
