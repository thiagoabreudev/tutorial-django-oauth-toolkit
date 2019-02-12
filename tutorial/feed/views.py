from django.shortcuts import render
from feed.models import Feed
from feed.serializers import FeedSerializer
from rest_framework import viewsets


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
