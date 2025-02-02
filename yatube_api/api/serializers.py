from rest_framework import serializers

from django.contrib.auth import get_user_model

from posts.models import Post, Group, Comment, Follow


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.SlugRelatedField(queryset=Group.objects.all(),
                                         slug_field='id',
                                         allow_null=True, default=None)

    class Meta:
        model = Post
        fields = ('__all__')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('__all__')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username", default=serializers.CurrentUserDefault(),
    )

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',)

    def validate_following(self, value):
        if value == self.context["request"].user:
            raise serializers.ValidationError()
        return value

    class Meta:
        model = Follow
        fields = ('__all__')
