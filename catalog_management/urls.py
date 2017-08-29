from django.conf.urls import patterns, include, url
from catalog_management.views import catalog_management


urlpatterns = patterns(
    "",
    # user management urls
    url(r'^(.*)/?$', catalog_management, name='catalog_management'),
)					