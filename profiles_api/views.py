from rest_framework.views import APIView
from rest_framework.response import Response

class HellloAPIView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'Lorem Ipsum is simply dummy text of the printing and',
            'typesetting industry. Lorem Ipsum has been the industry',
            'standard dummy text ever since the 1500s, when an unknown printer took a galley of type and ',
            'scrambled it to make a type specimen book. ',
            'It has survived not only five centuries'
        ]

        return Response({
            'msg':'Hello',
            'an_apiview': an_apiview
        })
