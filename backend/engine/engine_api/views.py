from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db import connection
from .models import ImportBookAuthors, ImportBooks, BuildWork
from .serializers import AuthorSerializer, BookSerializer, WorkSerializer


class SearchAuthor(APIView):

    def get(self, request):

        authors = ImportBookAuthors.objects.filter(name__icontains=request.GET.get('query')).order_by('-ratings_count')[:10]
        serializer = AuthorSerializer(authors, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AuthorDetails(APIView):

    def get(self, request, author_id: int):

        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         f"""
        #         SELECT *
        #         FROM IMPORT_AUTHORS
        #         INNER JOIN IMPORT_BOOKS
        #         WHERE AUTHOR_ID = '{author_id}'
        #         """
        #     )

        works = BuildWork.objects.raw(
            f"""
            SELECT *
            FROM BUILD_WORK
            WHERE AUTHOR_ID = '{author_id}'
            AND LANGUAGE_CODE LIKE '%eng%'
            ORDER BY BOOK_RATINGS_COUNT DESC
            LIMIT 10
            """
        )
        serializer = WorkSerializer(works, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SearchBook(APIView):

    def get(self, request):

        books = ImportBooks.objects.filter(title__icontains=request.GET.get('query')).order_by('-ratings_count')[:10]
        serializer = BookSerializer(books, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BookDetails(APIView):

    def get(self, request, work_id: int):

        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         f"""
        #         SELECT *
        #         FROM IMPORT_AUTHORS
        #         INNER JOIN IMPORT_BOOKS
        #         WHERE AUTHOR_ID = '{author_id}'
        #         """
        #     )

        # TODO: Figure out if we want to have multiple get requests to get similar books here??

        works = BuildWork.objects.raw(
            f"""
            SELECT *
            FROM BUILD_WORK
            WHERE WORK_ID = '{work_id}'
            AND LANGUAGE_CODE LIKE '%eng%'
            ORDER BY BOOK_RATINGS_COUNT DESC
            LIMIT 10
            """
        )
        serializer = WorkSerializer(works, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)
