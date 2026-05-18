from rest_framework import generics, status
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer
from .pagination import CustomPagination


# CREATE CATEGORY + BULK CREATE
class CategoryCreateAPIView(generics.CreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):

        # Check if request is bulk data
        many = isinstance(request.data, list)

        serializer = self.get_serializer(
            data=request.data,
            many=many
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success": True,
                "message": "Category created successfully",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


# RETRIEVE CATEGORY + PARENT + SUBCATEGORIES
class CategoryRetrieveAPIView(generics.ListAPIView):

    serializer_class = CategorySerializer
    pagination_class = CustomPagination

    def get_queryset(self):

        queryset = Category.objects.select_related(
            'parent'
        ).prefetch_related(
            'children'
        )

        # Search by category name
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(
                name__icontains=name
            )

        # LIMIT SUPPORT
        limit = self.request.query_params.get('limit')

        if limit:
            queryset = queryset[:int(limit)]

        return queryset