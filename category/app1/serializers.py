from rest_framework import serializers
from .models import Category


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):

    # SHOW PARENT DETAILS
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True
    )

    # SHOW CHILDREN
    subcategories = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'parent',
            'subcategories'
        ]

    def get_subcategories(self, obj):

        children = obj.children.all()

        return SubCategorySerializer(
            children,
            many=True
        ).data