from django.urls import path
from .views import BlogView

urlpatterns = [
    path("api/", BlogView.as_view(), name="blog"),

]
