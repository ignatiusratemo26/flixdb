from django.urls import path, include
# from watchlist.api import views
from watchlist.api.views import WatchlistListAV, WatchlistDetailAV

urlpatterns = [
    path('list/', WatchlistListAV.as_view(), name='watchlist'),
    path('<int:pk>/', WatchlistDetailAV.as_view() , name='watchlist-details')
]
