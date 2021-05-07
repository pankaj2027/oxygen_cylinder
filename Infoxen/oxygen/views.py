from rest_framework import status,viewsets
from rest_framework.response import Response

from .models import OxygenCylinder
from .serializers import OxygenCylinderSerializer


class OxygenCylinderDetail(viewsets.ViewSet):
    def create(self,request):
        serializer = OxygenCylinderSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data saved successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        oxygen_data = OxygenCylinder.objects.all().order_by('-TimeStamp')
        serializer = OxygenCylinderSerializer(oxygen_data, many=True)
        return Response(serializer.data)



