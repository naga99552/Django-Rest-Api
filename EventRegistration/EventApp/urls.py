from django.urls import  path,include
from .views import EventRegistration_list
from . apiviews import Eventlist,EventDetails,Usercreate_or_Registeruser,LoginApi,AccountDelete
urlpatterns=[

    path('EventApp/',Eventlist().as_view(), name="Event Registered list"),
    path('EventApp/',EventDetails().as_view(),name="Event Details"),
path('register/',Usercreate_or_Registeruser.as_view(),name="User Registration"),
path('login/',LoginApi().as_view(),name="Login"),
path('delete/',AccountDelete().as_view(),name="account delete")
]