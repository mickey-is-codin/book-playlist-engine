from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import ImportBookAuthorsKeyed
from .serializers import AuthorSerializer

class SearchAuthor(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Authors items for given searched string
        '''
        # query = request.GET.get('query')

        # authors = ImportBookAuthorsKeyed.objects.raw(
        #     """
        #     SELECT *
        #     FROM import_book_authors_keyed
        #     WHERE author_name 
        #     BETWEEN '' AND ''
        #     """
        # )
        authors = ImportBookAuthorsKeyed.objects.filter(author_name__icontains=request.GET.get('query')).order_by('-author_ratings_count')[:10]
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # # 2. Create
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