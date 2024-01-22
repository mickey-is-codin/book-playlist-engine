from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db import connection
from .models import ImportBookAuthors, ImportBooks
from .serializers import AuthorSerializer, BookSerializer


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

        books = ImportBooks.objects.raw(
            f"""
            SELECT *
            FROM IMPORT_AUTHORS
            INNER JOIN IMPORT_BOOKS
            USING(BOOK_ID)
            WHERE AUTHOR_ID = '{author_id}'
            AND LANGUAGE_CODE LIKE 'eng'
            ORDER BY RATINGS_COUNT DESC
            LIMIT 10
            """
        )
        serializer = BookSerializer(books, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SearchBook(APIView):

    def get(self, request):

        books = ImportBooks.objects.filter(title__icontains=request.GET.get('query')).order_by('-ratings_count')[:10]
        serializer = BookSerializer(books, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, name, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        authors = ImportBookAuthors.objects.raw(
            """
            SELECT *
            FROM IMPORT_BOOK_AUTHORS
            WHERE NAME LIKE %s
            """,
            [name]
        )
        serializer = AuthorSerializer(authors, many = True)
        print("==============PRINTING==============")
        print(serializer)
        print("====================================")
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Todo with given todo data
    #     '''
    #     data = {
    #         'task': request.data.get('task'), 
    #         'completed': request.data.get('completed'), 
    #         'user': request.user.id
    #     }
    #     serializer = TodoSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)