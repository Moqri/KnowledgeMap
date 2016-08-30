from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.paper_list, name='paper_list'),
    url(r'^search/$', views.search),
    url(r'^title/$', views.title),	
    url(r'^author/$', views.author),	
    url(r'^keyword/$', views.keyword),	
]