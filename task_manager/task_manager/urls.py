from django.urls import path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from tasks.views import RegisterView, LoginView, TaskViewSet


# Registering TaskViewSet with a router
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),  # Register the admin site
]

# Extend urlpatterns with the router's urls
urlpatterns += router.urls