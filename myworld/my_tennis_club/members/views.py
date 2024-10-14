from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FormData
from .serializers import FormDataSerializer
from django.shortcuts import render

# API view to handle form submissions
@api_view(['POST'])
def submit_form(request):
    serializer = FormDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to display stored data
def view_data(request):
    data = FormData.objects.all()
    return render(request, 'view_data.html', {'data': data})
