from rest_framework import routers
from feed.views import FeedViewSet

router = routers.DefaultRouter()
router.register(r'feed', FeedViewSet, base_name='feed')