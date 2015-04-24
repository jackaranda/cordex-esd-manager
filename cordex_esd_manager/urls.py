from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from experiments import views as experiment_views
from submissions import views as submission_views


router = routers.DefaultRouter()
router.register(r'timeperiods', experiment_views.TimePeriodViewSet)
router.register(r'datasets', experiment_views.DatasetViewSet)
router.register(r'meta-experiments', experiment_views.MetaExperimentViewSet)
router.register(r'experiments', experiment_views.ExperimentViewSet)

router.register(r'models', submission_views.ModelViewSet)
router.register(r'submissions', submission_views.SubmissionViewSet)
router.register(r'uploads', submission_views.UploadView)



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cordex_esd_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'web.views.index', name='index'),
    url(r'^projects/([-\w]+)/$', 'web.views.experiments', name='web-experiments'),
    url(r'^projects/([-\w]+)/([-\w]+)/([-\w]+)$', 'web.views.experiment_detail', name='web-experiment-detail'), 
    url(r'^submissions/([-\w]+)/([-\w]+)/([-\w]+)$', 'web.views.submissions', name='web-submissions'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(router.urls, namespace='rest')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^accounts/login', 'web.views.login_view', name='web-login'),
    url(r'^accounts/profile', 'web.views.user_profile', name='web-profile'),
    url(r'^accounts/logout', 'web.views.logout_view', name='web-logout'),

)
