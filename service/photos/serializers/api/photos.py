from rest_framework import serializers
from photos.models.photos import Photo
from photos.commons.tasks import resize_photo
from photos.commons.responses import success_response


class PhotoCreateSerializer(serializers.ModelSerializer):
    file = file = serializers.ImageField(write_only=True)
    id = serializers.UUIDField(read_only=True)
    
    class Meta:
        model = Photo
        fields = ('file', 'id',)


class PhotoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id', 'filename', 
                  'processing', 'processing_success')


class PhotoPartialUpdateSerializer(serializers.ModelSerializer):

    width = serializers.IntegerField(write_only=True)
    height = serializers.IntegerField(write_only=True)

    class Meta:
        model = Photo
        fields = ('id', 'height', 'width')

    def update(self, instance, validated_data):
        width = self.validated_data.pop('width')
        height = validated_data.pop('height')
        resize_photo.delay(width=width, height=height, id=instance.id)
        return success_response

class SuccessResponseSerializerMixin(serializers.Serializer):
    succes=serializers.BooleanField()