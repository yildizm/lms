from django.conf.urls import patterns, include, url
from auth.views import login, logout


urlpatterns = patterns(
    "",
    # user management urls
    url(r'^login/?$', login, name='login'),
    url(r'^logout/?$', logout, name='logout'),
)					