from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from experiments import views as experiment_views
from submissions import views as submission_views


router = routers.DefaultRouter()
router.register(r'timeperiods', experiment_views.TimePeriodViewSet)
router.register(r'datasets', experiment_views.DatasetViewSet)
router.register(r'experiments', experiment_views.ExperimentViewSet)

router.register(r'models', submission_views.ModelViewSet)
router.register(r'submissions', submission_views.SubmissionViewSet)
router.register(r'uploads', submission_views.UploadView)



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cordex_esd_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'web.views.index', name='index'),
    url(r'^experiments', 'web.views.experiments', name='experiments'),
    url(r'^submissions', 'web.views.submissions', name='submissions'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
