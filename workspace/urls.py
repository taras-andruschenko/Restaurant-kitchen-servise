from django.urls import path

from workspace.views import index


urlpatterns = [
    path("", index, name="index"),
]


app_name = "workspace"
