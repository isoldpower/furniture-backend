import os.path
from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile

size = (128, 128)

def get_compressed_image(origin):
    try:
        image = Image.open(origin)
        image.thumbnail(size)
        thumb_io = BytesIO()
        image.save(thumb_io, image.format, quality=5)
        return ContentFile(thumb_io.getvalue())
    except Exception as e:
        return origin

def get_compressed_name(origin):
    file_name, file_extension = os.path.splitext(origin.name)
    return file_name + '_low' + file_extension
