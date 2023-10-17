from rest_framework import serializers
from .models import ImagePredictModel

class ImagePredictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImagePredictModel
        fields = '__all__'