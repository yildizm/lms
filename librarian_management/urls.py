from django.conf.urls import patterns, include, url
from librarian_management.views import librarian_management


urlpatterns = patterns(
    "",
    # user management urls
    url(r'^(.*)/?$', librarian_management, name='librarian_management'),
)					