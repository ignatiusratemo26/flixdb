from django.urls import path, include
# from watchlist.api import views
from watchlist.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watchlist'),
    path('<int:pk>/', WatchListDetailAV.as_view() , name='watchlist-details'),
    path('stream/', StreamPlatformAV.as_view(), name='streamplatforms'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform'),

]
