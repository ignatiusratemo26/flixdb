from rest_framework import serializers
from watchlist.models import Watchlist, StreamPlatform

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields= '__all__'
        # if you want to define what you want to be seen
        # fields= ['id', 'name', 'active']
        # exclude = ['active']

class StreamPlatformSerializer(serializers.ModelSerializer):
    # from the related name 'watchlist' in models
    watchlist = WatchlistSerializer(many= True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
