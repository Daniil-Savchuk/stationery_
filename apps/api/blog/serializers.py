from rest_framework import serializers

from apps.blog.models import Article, BlogCategory, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        madel = Tag
        fields = (
            'id',
            'name',
        )


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = (
            'id',
            'name',
            'image',
        )


class ArticleWriteSerializer(serializers.ModelSerializer):
    tag = serializers.ListField(child=serializers.CharField(max_length=64))

    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'image',
            'title',
            'text_preview',
            'text',
            'publish_date',
            'tag'
        )


class ArticleReadSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(many=True)
    tag = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'image',
            'user',
            'title',
            'text_preview',
            'text',
            'publish_date',
            'created_at',
            # 'image_thumbnail'
            'tag'
        )
