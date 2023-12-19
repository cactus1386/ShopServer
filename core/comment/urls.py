from django.urls import path
from .views import CommentsView

urlpatterns = [
    path('api/comments/', CommentsView.as_view()),
]
