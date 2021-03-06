from django.http import JsonResponse
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from api.serializers import UserDataSerializer
from webapp.models import UserData


class OrderView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        orders = UserData.objects.all()
        response_data = UserDataSerializer(orders, many=True).data
        return JsonResponse(data=response_data, safe=False)

    def post(self, request):
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return super(OrderView, self).get_permissions()
