from django.test import TestCase

from backend.models import Trap_Image as Image

from .opencv_library import b64_2_img

image = Image.objects.get(pk=30)
print(b64_2_img(image.image))
