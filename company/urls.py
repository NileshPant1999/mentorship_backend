from django.urls import path
from .views import CategoryList, CompanyDetailsView, CreateCompany, PostList

app_name = "users"

urlpatterns = [
    path("details/<int:pk>/", CompanyDetailsView.as_view(), name="getcompany"),
    path("create/", CreateCompany.as_view(), name="createcompany"),
    path("post", PostList.as_view(), name="getpost"),
    path("category", CategoryList.as_view(), name="getcategory"),
]
