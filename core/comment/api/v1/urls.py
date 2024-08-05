from django.urls import path, include
from . import views

app_name = "api-v1"

urlpatterns = [
    path("v1/post", views.CommentsView.as_view(), name="comments"),
    path("v1/post/<int:pk>/", views.CommentDetailView.as_view(),
         name="comments-detail"),

]
