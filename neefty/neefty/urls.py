from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'neefty.views.home', name='home'),
    url(r'^logout/$', 'neefty.views.logout_view', name='logout'),
    url(r'^urlencode/$', 'neefty.views.urlencode', name='urlencode'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('^dimension/add/$', 'neefty.views.add_dimension', name='add_dimension'),
    url('^item/add/$', 'neefty.views.add_list_item', name='add_list_item'),
    
    # url(r'^neefty/', include('neefty.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
