from rest_framework import serializers

from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    text = serializers.CharField(required=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('author', 'pub_date', 'author')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title',)
        read_only_fields = ('id',)
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created',)
        read_only_fields = ('id', 'author', 'created',)
        model = Comment
