from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

# from rest_framework_json_api.relations import ResourceRelatedField

from conferences.models.talks import Talk


class TalkSerializer(ModelSerializer):
    class Meta:
        model = Talk
        fields = (
            "id",
            "nombre",
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }