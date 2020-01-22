from django.conf.urls import include, url

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework import VERSION

from nine import versions

from foo.viewsets import FooViewSet

admin.autodiscover()

urlpatterns = [
    # # foo URLs:
    # url(r'^foo/', include('foo.urls')),
]

if versions.DJANGO_GTE_2_0:
    urlpatterns += [
        url(r'^admin/', admin.site.urls),
    ]
else:
    urlpatterns += [
        url(r'^admin/', include(admin.site.urls)),
    ]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


__title__ = 'fobi.contrib.apps.drf_integration.urls'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'urlpatterns',
    'fobi_router',
)

DRF_VERSION = [int(_v) for _v in VERSION.split('.')]
basename = 'basename'
if DRF_VERSION[:2] < [3, 10]:
    basename = 'base_name'

router_kwargs = {basename: 'fooapi'}

foo_router = DefaultRouter()
foo_router.register(
    r'fooapi',
    FooViewSet,
    **router_kwargs
)
urlpatterns = foo_router.urls
