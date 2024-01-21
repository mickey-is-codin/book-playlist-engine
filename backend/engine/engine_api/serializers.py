from rest_framework import serializers
from .models import ImportBookAuthors, ImportBooks

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportBooks
        fields = ["title", "book_id", "work_id", "image_url", "text_reviews_count", 'ratings_count', 'num_pages', 'publisher', 'description', 'format', 'average_rating']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportBookAuthors
        fields = ["author_id", "name", "average_rating", "ratings_count", "text_reviews_count"]
