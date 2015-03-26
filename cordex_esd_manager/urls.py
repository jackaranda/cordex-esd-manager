from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from submissions import views


router = routers.DefaultRouter()
router.register(r'datasets', views.DatasetViewSet)



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cordex_esd_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'web.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
