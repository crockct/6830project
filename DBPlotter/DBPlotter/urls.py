from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from DBPlotter import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DBPlotter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pie_chart/', 'DBPlotter.views.pie_chart', name='pie_chart'),
    url(r'^bubble_cloud/', TemplateView.as_view(template_name='bubble_cloud/index.html')),
    url(r'^get_tables/', 'DBPlotter.views.get_tables', name='get_tables'),
    url(r'^make_queries/', 'DBPlotter.views.make_queries', name='make_queries'),
    url(r'^get_queries/', 'DBPlotter.views.get_queries', name='get_queries'),
    url(r'^process_query/', 'DBPlotter.views.process_query', name='process_query'),
    url(r'^close/', 'DBPlotter.views.close', name='close'),
)

urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static'}
))
