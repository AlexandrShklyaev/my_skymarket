from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from ads.views import AdViewSet, CommentViewSet

# TODO настройка роутов для модели

router_ads = SimpleRouter()
router_ads.register(r"ads", AdViewSet)

# router.register("ads", AdViewSet, basename="users")
router_com = NestedSimpleRouter(router_ads, r"ads", lookup="ad")
router_com.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(router_ads.urls)),
    path("", include(router_com.urls)),

    ]