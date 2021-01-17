from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APIView"""

    def get(self, request, format=None):
        an_apiview = [
        'get, post, patch, put, delete',
        'Is similar to a traditional Djago View',
        'Gives you the most control over your application logic',
        'Fokume'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
