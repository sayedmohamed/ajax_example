from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ajax_example.views.home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ajax_results/(?P<type>.+)$','ajax_example.views.ajax_results'),
    url(r'^admin/', include(admin.site.urls)),
)
