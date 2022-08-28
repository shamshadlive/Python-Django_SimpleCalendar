
from django.urls import path
from . import views

urlpatterns = [
    path('', views.btspcalendar, name="btspcalendar"),
    path('prevOrNextMonth', views.prevOrNextMonth, name="prevOrNextMonth"),
  

    ]
