"""mypro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from emploapp import views
from rest_framework import routers
# from emploapp.views import Emploviewset
from emploapp.views import StudViewset
from rest_framework.urlpatterns import format_suffix_patterns
# router = routers.SimpleRouter()
# router = routers.DefaultRouter()
# router.register(r'studrouter', StudViewset, basename='studd')

studlist = StudViewset.as_view({
    'get': 'list'
})

studdetail = StudViewset.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', views.api_root),

    path('genericstudlist', views.GenericstudListCreate.as_view(), name='generic-studlist'),
    path('studelist', views.Studentlist.as_view(), name='stude-list'),
    path('emplolist', views.Emplolist.as_view(), name='emplo-list'),
    path('studelist/<int:pk>', views.Studentdetail.as_view(), name='stude-detail'),
    path('emplolist/<int:pk>', views.Emplodetail.as_view(), name='emplo-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),

    path('emplist/', views.Emplist.as_view(), name='emp-list'),
    path('emplist/<int:pk>', views.Empdetail.as_view(), name='emp-detail'),
    path('empupdate/<int:pk>', views.Empupdate.as_view(), name='emp-update'),
    path('empdelete/<int:pk>', views.Empdelete.as_view()),

    path('emplistmixins/', views.EmplistMixins.as_view()),
    path('empdetailedmixins/<int:pk>', views.EmpdetailedMixins.as_view(), name='empdetailed-mixins'),

    path('genericemplist', views.GenericempListCreate.as_view(), name='generic-emplist'),
    path('genericempupdateretrievedelete/<int:pk>', views.GenericempRetrieveUpdateDelete.as_view()),

    path('viewsets/', studlist, name='stud-list'),
    path('viewsets/<int:pk>', studdetail, name='stud-detail'),

    path('studlist', views.Studlist, name='stud-list'),
    path('studlist/<int:pk>', views.Studdetail),
    path('studcreate', views.Studcreate, name='stud-create'),
    path('studupdate/<int:pk>', views.Studupdate),
    path('studdelete/<int:pk>', views.Studdelete),

    path('custlist/', views.Custlist.as_view(), name='cust-list'),
    path('custlist/<int:pk>', views.Custdetail.as_view(), name='cust-detail'),
    path('custupdate/<int:pk>', views.Custupdate.as_view(), name='cust-update'),
    path('custdelete/<int:pk>', views.Custdelete.as_view()),



    # path('', include(router.urls)),

])
# urlpatterns += router.urls
print("all url", urlpatterns)


# urlpatterns = format_suffix_patterns(urlpatterns)