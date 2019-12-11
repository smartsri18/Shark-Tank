from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company, Product
from .serializers import CompanySerializer, ProductSerializer

#FETCH COMPANY DETAIL
class SearchView(APIView):
    def get(self,request):
        season = request.data.get('season')
        episode = request.data.get('episode')
        investors = request.data.get('investors')
        investors_amt = request.data.get('investors_amt')
        gender = request.data.get('gender')

        # FILTER OPTIONS FOR AND AND OR LOGIC
        kwargs = {}
        if season:
            kwargs['season'] = season
        if episode:
            kwargs['episode'] = episode
        if investors_amt:
            kwargs['amount'] = investors_amt
        if gender:
            kwargs['gender'] = gender

        if investors:
            product_det = Product.objects.filter(investors=investors).values('company_name','product_name','company_name_id')
            kwargs['id'] = product_det[0]['company_name_id']

        # GETTING COMPANY DETAILS
        company_det = Company.objects.all().filter(**kwargs)
        serializer = CompanySerializer(company_det, many=True)
        return Response({"company_det": serializer.data})
