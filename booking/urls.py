from django.urls import path, include

from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('account/', include('django.contrib.auth.urls'), name='login'),
    path('about', views.about, name='about'),
    path('roomlist', views.RoomList.as_view(), name='room_list'),
    path('guestlist', views.GuestList.as_view(), name='guest_list'),
    path('guestcreate', views.GuestCreate.as_view(), name="guest_create"),
    path('guestupdate/<pk>', views.GuestUpdate.as_view(), name="guest_update"),
    path('guestdelete/<pk>', views.GuestDelete.as_view(), name="guest_delete"),
    path('staycreate', views.StayCreate.as_view(), name="stay_create"),

]