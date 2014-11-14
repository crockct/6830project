from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from DBPlotter import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DBPlotter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pie_chart/', 'DBPlotter.views.pie_chart', name='pie_chart'),
)

urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static'}
))
