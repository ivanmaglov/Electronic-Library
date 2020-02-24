"""electorniclibrary2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from library.writer_views import WriterSignUpView
from library.reader_views import ReaderSignUpView
from library.library_views import SignUpView
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/reader/', ReaderSignUpView.as_view(), name='reader_signup'),
    path('accounts/signup/writer/', WriterSignUpView.as_view(), name='writer_signup'),
    path('api/', include('library.api.urls', namespace='api')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
