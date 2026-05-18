from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):

    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):

        return Response({
            "page": self.page.number,
            "page_size": self.page.paginator.per_page,
            "total_count": self.page.paginator.count,
            "results": data
        })