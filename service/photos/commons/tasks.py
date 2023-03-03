from celery import shared_task
from PIL import Image
from service.settings import MEDIA_ROOT
from photos.models.photos import Photo


@shared_task
def resize_photo(width, height, id, ):
    try:
        instance = Photo.objects.get(id=id)
        setattr(instance, 'processing', True)
        instance.save()
        img = Image.open((f"{MEDIA_ROOT}/photos/{instance.filename()}"))
        size = (width, height)
        out = img.resize(size)
        out.save(f"{MEDIA_ROOT}/photos/{instance.filename()}")
        setattr(instance, 'processing_success', True)
        instance.save()
    except Exception as err:
        if instance:
            setattr(instance, 'processing_success', False)
            instance.save()
        print(err)
    finally:
        setattr(instance, 'processing', False)
        instance.save()
