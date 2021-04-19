from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from resources.models import Resources

from resources.serializers import ResourcesSerializer


class ResourcesView(APIView):
    def get(self, request):
        return_data = dict()
        data = Resources.objects.all()
        return_data['resorces'] = ResourcesSerializer(data, many=True).data
        return_data['total_count'] = len(return_data.get('resources', []))
        return Response(
            data=return_data,
            status=200
        )

    def post(self, request):
        resource_data = request.data
        serializer = ResourcesSerializer(data=resource_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            data=serializer.data,
            status=200
        )

    def put(self, request):
        pk = request.query_params.get("id", None)
        saved_article = get_object_or_404(Resources.objects.all(), pk=pk)
        data = request.query_params
        serializer = ResourcesSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(
            {"message": "Updated"},
            status=200
        )

    def delete(self, request):
        pk = request.query_params.get("id", None)
        resource = get_object_or_404(Resources.objects.all(), pk=pk)
        resource.delete()
        return Response(
            {"message": f"Deleted {pk} resource"},
            status=204)
