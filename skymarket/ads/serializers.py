from phonenumber_field import serializerfields
from rest_framework import serializers

from ads.models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    ad_id = serializers.ReadOnlyField(source="ad.id")
    author_f_name = serializers.ReadOnlyField(source="author.first_name")
    author_l_name = serializers.ReadOnlyField(source="author.last_name")

    class Meta:
        model = Comment
        fields = ("pk", "text", "author_id", "ad_id", "author_f_name", "author_l_name", "created_at")


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    author_f_name = serializers.ReadOnlyField(source="author.first_name")
    author_l_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)
    author_id = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Ad
        fields = (
            "pk", "image", "title", "price", "phone", "author_f_name", "author_l_name", "description", "author_id")
