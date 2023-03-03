import os
import uuid

from django.db import models


class Photo(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4, editable=False
    )

    file = models.ImageField(
        upload_to='photos',
        null=False,
        blank=False,
    )

    processing = models.BooleanField(
        default=False
    )

    processing_success = models.BooleanField(
        default=None,
        null=True,
        blank=True
    )

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return f'{self.id})'

    class Meta:
        pass
