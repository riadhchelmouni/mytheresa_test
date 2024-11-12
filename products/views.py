from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()

        # Filter by category if provided
        category = request.query_params.get('category')
        if category:
            products = products.filter(category=category)
        
        # Filter by priceLessThan if provided
        price_less_than = request.query_params.get('priceLessThan')
        if price_less_than:
            products = products.filter(price__lte=int(price_less_than))
        
        products = products[:5]

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
