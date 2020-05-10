from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)
# router.register(r'containers', views.GetContainers)
#router.register(r'test', views.GetContainers, basename='test')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'tests/', views.GetContainers.as_view(), name="tests"),
    path(r'tests/#', views.start_container),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
