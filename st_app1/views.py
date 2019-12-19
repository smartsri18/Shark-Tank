from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import api_view


from .models import Company, Product, Episode
from .serializers import CompanySerializer, ProductSerializer

# View for Investors invested in the product : Company name
@api_view(['GET', 'POST'])
def get_or_post(request):
    season = request.data.get('season')
    episode = request.data.get('episode')
    investors = request.data.get('investors')
    investors_amt = request.data.get('investors_amt')
    gender = request.data.get('gender')

    # FILTER OPTIONS FOR AND AND OR LOGIC
    kwargs = {}

    if episode:
        showlist = Episode.objects.get(season= season ,episode_number=episode)
        kwargs['showlist'] = showlist

    if investors_amt:
        kwargs['amount'] = investors_amt

    if gender:
        kwargs['gender'] = gender

    company_list = []
    if investors:
        product_det = Product.objects.all().filter(investors=investors).values('company_name')
        for item in product_det:
            company_list.append(item['company_name'])
        # Grabing the investors from product table
        if season:
            # Fetching investors from specific season
            company_det = Company.objects.all().filter(**kwargs,pk__in=company_list,showlist__season=season,deal="Yes")
        else:
            # Fetching ivestors from all season
            company_det = Company.objects.all().filter(**kwargs,pk__in=company_list,deal="Yes")
    else:
        # If investors field is not used for filter
        if season and not episode:
            company_det = Company.objects.all().filter(showlist__season=season,deal="Yes")
        else:
            company_det = Company.objects.all().filter(**kwargs, deal="Yes")

    # GETTING COMPANY DETAILS
    serializer = CompanySerializer(company_det, many=True)
    return Response({"company_det": serializer.data})
