from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from resources.models import Resources

from resources.serializers import ResourcesSerializer


class ResourcesView(APIView):
    def get(self, request):
        '''
        Метод получения всех материалов
        :param request:
        :return: Response
        '''
        return_data = dict()
        data = Resources.objects.all()
        return_data['resorces'] = ResourcesSerializer(data, many=True).data
        return_data['total_count'] = len(return_data.get('resources', []))
        return Response(
            data=return_data,
            status=200
        )

    def post(self, request):
        '''
        Метод создания метриала
        :param request:
        :return:
        '''
        resource_data = request.data
        serializer = ResourcesSerializer(data=resource_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            data=serializer.data,
            status=201
        )

    def put(self, request):
        '''
        Метод обновления материала по id в параметрах
        и отстальных данных в параметрах
        :param request:
        :return: Response
        '''
        pk = request.query_params.get("id", None)
        saved_article = get_object_or_404(Resources.objects.all(), pk=pk)
        data = request.query_params
        serializer = ResourcesSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(status=204)

    def delete(self, request):
        '''
        Удаление материала по id в параметре
        :param request:
        :return: Response
        '''
        pk = request.query_params.get("id", None)
        resource = get_object_or_404(Resources.objects.all(), pk=pk)
        resource.delete()
        return Response(status=204)
