from django.urls import path

from workspace.views import index


urlpatterns = [
    path("", index, name="index"),
    path("")
]


app_name = "workspace"
