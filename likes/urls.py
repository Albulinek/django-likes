from django.conf.urls import patterns, url

from likes import views


urlpatterns = [
    url(
        r"^like/(?P<content_type>[\w-]+)/(?P<id>\d+)/(?P<vote>-?\d+)/$",
        views.like,
        name="like"
    )
]
