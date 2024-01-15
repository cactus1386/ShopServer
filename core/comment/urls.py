from django.urls import path, include

app_name = 'comments'

urlpatterns = [
    path('api/', include('comment.api.v1.urls')),
]
