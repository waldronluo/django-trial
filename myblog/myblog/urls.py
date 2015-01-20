from django.conf.urls import include, url
from django.contrib.staticfiles import views
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^blog/', include('blog.urls')),
    url(r'^privatesite/', include('privatesite.urls')),
    #url(r'^static.*', views.serve),
]
