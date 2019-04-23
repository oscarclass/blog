from django.urls import path
from . import views

app_name = "blog"


urlpatterns = [
        path("", views.IndexView.as_view(), name="index"),
        path("detail/<int:pk>/", views.DetailAndCreate.as_view(),name="detail"),
        path("category/<int:pk>", views.CategoryView.as_view(), name="category"),
        path("stablepage/<int:pk>", views.StablePageView.as_view(), name="stablepage"),
        ]