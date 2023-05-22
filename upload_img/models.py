from django.db import models
from django.core.files.storage import default_storage
import uuid
import os


# Create your models here.
def get_path_img(instance, filename):
    folder_root = "test"
    filename = f"image_{uuid.uuid4().hex[:6]}.png"
    models_name = instance.__class__.__name__.lower()
    if instance.id:
        folder_name = str(instance.id)
    return os.path.join(folder_root, models_name, folder_name, filename)


class Img(models.Model):
    img = models.ImageField(upload_to=get_path_img, storage=default_storage)
