from .views import (
    CreateProgress,
    EditProgress,
    FounderDetails,
    CreateFounder,
    ProgressDetails,
    ProgressList,
    EditFounder,
)
from django.urls import path

app_name = "founders"

urlpatterns = [
    path("details/<str:pk>/", FounderDetails.as_view(), name="founderdetail"),
    path("create/", CreateFounder.as_view(), name="createfounder"),
    path("progress/<int:pk>/", ProgressList.as_view(), name="progresslist"),
    path("progress/edit/<int:pk>/", EditProgress.as_view(), name="editprogress"),
    path("edit/<int:user>/", EditFounder.as_view(), name="editfounder"),
    path("add/", CreateProgress.as_view(), name="createprogress"),
    path(
        "progress/details/<int:slug>/",
        ProgressDetails.as_view(),
        name="progressdetails",
    ),
]
