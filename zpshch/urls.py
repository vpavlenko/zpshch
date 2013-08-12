from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mainapp.views.home', name='home_url'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^([a-z]+)/$', 'mainapp.views.board', name='board_url'),
    url(r'^change_rating/$', 'mainapp.views.change_rating', name='change_rating'),
    url(r'^add_comment/$', 'mainapp.views.add_comment', name='add_comment'),
)
