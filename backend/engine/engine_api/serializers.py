# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import ImportBookAuthorsKeyed

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportBookAuthorsKeyed
        fields = ["author_id", "author_name", "author_average_rating", "author_text_reviews_count", "author_ratings_count"]