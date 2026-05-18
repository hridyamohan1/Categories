from django.urls import path

from .views import (
    CategoryCreateAPIView,
    CategoryRetrieveAPIView
)

urlpatterns = [

    path(
        'categories/create/',
        CategoryCreateAPIView.as_view()
    ),

    path(
        'categories/',
        CategoryRetrieveAPIView.as_view()
    ),
]