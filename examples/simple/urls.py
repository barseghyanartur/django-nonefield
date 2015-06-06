from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

from fobi.settings import DEFAULT_THEME

admin.autodiscover()

# Mapping.
fobi_theme_home_template_mapping = {
    'bootstrap3': 'home/bootstrap3.html',
    'foundation5': 'home/foundation5.html',
}

# Get the template to be used.
fobi_home_template = fobi_theme_home_template_mapping.get(DEFAULT_THEME, 'home/base.html')

urlpatterns = patterns('',
    # django-fobi URLs:
    url(r'^fobi/', include('fobi.urls')),

    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # django-registration URLs:
    (r'^accounts/', include('registration.backends.default.urls')),

    # foo URLs:
    url(r'^foo/', include('foo.urls')),

    url(r'^$', TemplateView.as_view(template_name=fobi_home_template)),

    # django-fobi public forms contrib app:
    #url(r'^', include('fobi.contrib.apps.public_forms.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
