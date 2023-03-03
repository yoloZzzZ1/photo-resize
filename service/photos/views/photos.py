from rest_framework import viewsets, mixins
from photos.serializers.api import photos as photo_s
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse
from photos.models.photos import Photo
from photos.commons.responses import success_response


@extend_schema_view(
    create=extend_schema(
    summary='Добавить фото',
    tags=['Фото'],
    responses={200:OpenApiResponse(response=photo_s.PhotoCreateSerializer)
    }
),
    partial_update=extend_schema(
    summary='Изменить фото',
    tags=['Фото'],
    responses={
        200:OpenApiResponse(response=photo_s.SuccessResponseSerializerMixin)
    },
),
    retrieve=extend_schema(summary='Деталка фото', tags=['Фото']),
    destroy=extend_schema(
    summary='Удалить фото',
    tags=['Фото'],
    responses={
        200:OpenApiResponse(response=photo_s.SuccessResponseSerializerMixin)
    },
),
)
class PhotoViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Photo.objects.all()
    default_serializer_class = photo_s.PhotoCreateSerializer
    multi_serializer_classs = {
        'create':photo_s.PhotoCreateSerializer,
        'retrieve':photo_s.PhotoDetailSerializer,
        'partial_update': photo_s.PhotoPartialUpdateSerializer
    }
    http_method_names = ('get', 'post', 'patch', 'delete')

    def get_serializer_class(self):
        return self.multi_serializer_classs.get(self.action, self.default_serializer_class)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return success_response
