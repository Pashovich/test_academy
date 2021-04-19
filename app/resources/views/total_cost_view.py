from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum

from ..models import Resources



class TotalCostView(APIView):
    def get(self, request):
        data = Resources.objects.aggregate(total_cost=Sum('cost'))
        data['total_cost'] = 0 if data['total_cost'] is None else data['total_cost']
        return Response(
            data=data,
            status=200
        )
