from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import ImportBookAuthors, ImportBooks
from .serializers import AuthorSerializer, BookSerializer


class SearchAuthor(APIView):
    def get(self, request):
        authors = ImportBookAuthors.objects.raw(
            """
            SELECT *
            FROM IMPORT_BOOK_AUTHORS
            WHERE NAME LIKE %s
            """,
            [request.GET.get('query')]
        )
        serializer = AuthorSerializer(authors, many = True)
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