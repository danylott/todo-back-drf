from rest_framework.routers import DefaultRouter

from todolist.views import TaskViewSet

router = DefaultRouter()

router.register("tasks", TaskViewSet)


urlpatterns = router.urls
