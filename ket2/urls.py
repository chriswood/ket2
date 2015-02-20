from django.conf.urls import patterns, include, url
from django.contrib import admin
from ketapp.views import user, register_success, logout_view, post, user_edit
from ketapp.views import post_delete, post_edit, weather, comment

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ket2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'ketapp.views.index'),
    url(r'^limit/(?P<p_count>\d+)/$', 'ketapp.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^logout/', logout_view),
    url(r'^user/create', user),
    url(r'^user/edit', user_edit),
    url(r'^user/success', register_success),
    url(r'^post/create', post),
    url(r'^post/delete', post_delete),
    url(r'^post/edit/(?P<p_id>\d+)/$', post_edit),
    url(r'^post/edit/$', post_edit),
    url(r'^comment/save/$', comment),
    url(r'^weather/$', weather),
)
