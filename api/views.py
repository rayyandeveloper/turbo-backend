from django.shortcuts import render
import json


from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

from shop.models import MoneyHistory, Product


from .authentication import TokenAuthentication
from .models import Token, Shop
from .serializers import MoneyHistorySerializer, ProductSerializer, ShopLoginSerializer, ShopSerializer, TokenSerializer


@api_view(['POST'])
def login(request):

    setializer = ShopLoginSerializer(data=request.POST)

    if setializer.is_valid():
        shop = Shop.objects.get(
            name=setializer.data['name'], password=setializer.data['password'])
        token = Token.objects.create(
            shop=shop, device=setializer.data['device'])

        return Response({'token': token.key, 'shop': ShopSerializer(shop).data}, status=200)
    else:
        return Response(setializer.errors, status=400)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def products(request):
    products = Product.objects.filter(shop=request.user)
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_tokens(request, shop_id):
    tokens = Token.objects.filter(shop=shop_id)
    serializer = TokenSerializer(tokens, many=True)
    return Response(serializer.data, status=200)


@api_view(['DELETE'])
def delete_token(request, token_id):

    Token.objects.get(key=token_id).delete()

    return Response(status=204)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
def money_histories(request, pk):
    product = Product.objects.get(pk=pk)
    queryset = MoneyHistory.objects.filter(product=product)

    serializer = MoneyHistorySerializer(queryset, many=True)
    
    response = serializer.data

    filter = request.GET.get('filter')
    
    if filter:
        result = {}

        if filter == 'month':

            for mh in queryset:
                month = mh.created_at.month

                if month not in result:
                    result[month] = []

                result[month].append(mh)

        response = map(lambda x: MoneyHistorySerializer(x, context={'request': request}, many=True).data, result.values())


    return Response(response, status=200)
