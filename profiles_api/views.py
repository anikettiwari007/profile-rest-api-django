from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HellloAPIView(APIView):
    serializer_class = serializers.HelloSerializer

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

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                'msg':message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
