from django.conf.urls import url
from weather import views
 
urlpatterns = [
    url(r'^$', views.MainPage.as_view())
]