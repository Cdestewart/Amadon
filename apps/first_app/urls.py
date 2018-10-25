from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^amadon$', views.index),
    url(r'^amadon/cart$', views.show),
     url(r'^amadon/buy$', views.buy)
]