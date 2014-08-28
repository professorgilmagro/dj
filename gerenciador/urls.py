from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gerenciador.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # agenda
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'agenda.views.index'),
    url(r'^agenda/lista/', 'agenda.views.listing'),
    url(r'^agenda/adiciona/', 'agenda.views.create'),
    url(r'^agenda/item/(?P<pk_value>\d+)/$', 'agenda.views.edit'),
    url(r'^agenda/remove/(?P<pk_value>\d+)/$', 'agenda.views.delete'),

    # autenticacao
    url(r'^login/$', 'django.contrib.auth.views.login',
        {"template_name": "login.html"}),

    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        {"login_url": "/login"}),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
