"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls


from rest_framework.routers import DefaultRouter



schema_view = get_swagger_view(title='API')

urlpatterns = [
    url(r'^docs/', include_docs_urls(title='API documentation', public=False)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

if settings.ADMIN_ENABLED:
    urlpatterns += [
        url(r'^admin/', admin.site.urls)
    ]


urlpatterns += i18n_patterns(
    url(r'^swagger/$', schema_view),
    url(r'^user/', include('apps.notification_user.urls')),
    url(r'^sender/', include('apps.sender.urls')),
)