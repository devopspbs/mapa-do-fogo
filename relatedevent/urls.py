from django.conf.urls import url
from relatedevent import views

urlpatterns = [
    url(r'^reportedevents/$',
        views.ReportedEventList.as_view(),
        name=views.ReportedEventList.name),
    url(r'^reportedevents/(?P<pk>[0-9a-zA-Z]+)$',  
        views.ReportedEventDetail.as_view(), 
        name=views.ReportedEventDetail.name),        
    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name)
]