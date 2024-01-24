from django.urls import path
from .views import (
    SearchAuthor,
)

urlpatterns = [
    path('search/author', SearchAuthor.as_view()),
]