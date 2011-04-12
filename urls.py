from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

from eve_map.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # This is the entry you'd need if you just wanted to serve a proxy.
    # You'll need to create another site if you want to serve this alongside
    # other content.
    #(r'^', include('eve_proxy.urls')),

    url(r'^systemcloud.asc', ascsystems),
)

# If you'd like to serve media files via Django (strongly not recommended!),
# open up your settings.py file and set SERVE_MEDIA_LOCAL to True. This is
# appropriate on a developing site, or if you're running Django's built-in
# test server. Normally you want a webserver that is optimized for serving
# static content to handle media files (apache, lighttpd).
if settings.SERVE_MEDIA_LOCAL:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
