from django.http import HttpResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


def hello(request):
    return HttpResponse("Hello, World!")

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message': "Hello, Rest API!"}
    return Response(data)