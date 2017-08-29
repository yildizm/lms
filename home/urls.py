from django.conf.urls import patterns, include, url
from home.views import home


urlpatterns = patterns(
    "",
    # user management urls
    url(r'^.*$', home, name='home'),
)					