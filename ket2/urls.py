from django.conf.urls import patterns, include, url
from django.contrib import admin
from ketapp.views import user, register_success, logout, post, user_edit

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ket2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'ketapp.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^logout/', logout),
    url(r'^user/create', user),
    url(r'^user/success', register_success),
    url(r'^post/create', post),
    url(r'^user/edit', user_edit),
)
