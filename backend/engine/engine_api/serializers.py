from rest_framework import serializers
from .models import ImportBookAuthors, ImportBooks, BuildWork

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportBooks
        fields = ["title", "book_id", "work_id", "image_url", "text_reviews_count", 'ratings_count', 'num_pages', 'publisher', 'description', 'format', 'average_rating']

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildWork
        fields = ["title", "book_id", "work_id", "image_url", "book_text_reviews_count", 'book_ratings_count', 'num_pages', 'publisher', 'book_desc', 'format', 'book_average_rating']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportBookAuthors
        fields = ["author_id", "name", "average_rating", "ratings_count", "text_reviews_count"]
