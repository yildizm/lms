from django.conf.urls import patterns, include, url
from patron_management.views import patron_management


urlpatterns = patterns(
    "",
    # user management urls
    url(r'^(.*)/?$', patron_management, name='patron_management'),
)					