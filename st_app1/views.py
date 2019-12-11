from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import api_view


from .models import Company, Product
from .serializers import CompanySerializer, ProductSerializer

@api_view(['GET', 'POST'])
def get_or_post(request):
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
        print(product_det)
        kwargs['id'] = product_det[0]['company_name_id']

    # GETTING COMPANY DETAILS
    company_det = Company.objects.all().filter(**kwargs)
    serializer = CompanySerializer(company_det, many=True)
    print(serializer)
    return Response({"company_det": serializer.data})
