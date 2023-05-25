from django.urls import path, include
from .views import (
    AppListApiView,
)

urlpatterns = [
    path('/', AppListApiView.as_view()),
]