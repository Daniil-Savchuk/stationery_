from rest_framework import serializers

from apps.blog.models import Article


class BlogSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(write_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'user',
            'image',
            'title',
            'text_preview',
            'text',
        )


class BlogWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'user',
            'image',
            'title',
            'text_preview',
            'text',
        )


class BlogReadSerializer(serializers.ModelSerializer):
    categories = BlogSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'user',
            'image',
            'title',
            'text_preview',
            'text',
        )
