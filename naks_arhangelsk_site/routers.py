from rest_framework import routers
from mainapp.viewsets import MenuViewSet, PostViewSet

router = routers.DefaultRouter()

router.register(r'menu', MenuViewSet)
router.register(r'post', PostViewSet)