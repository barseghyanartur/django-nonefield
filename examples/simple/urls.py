from django.conf.urls import include, url

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from nine import versions

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
