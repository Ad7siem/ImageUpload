from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from PIL import Image
from io import BytesIO


###########################################################
### Creation of a model to assign a user type to a user ###
###########################################################
class UserProfile(models.Model):
    USER_TYPE = (
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('enterprise', 'Enterprise'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE)


###########################################################
########## Creation of a model with image storage #########
###########################################################
class Images(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_200px = models.ImageField(upload_to='images/200px/', null=True, blank=True)
    image_400px = models.ImageField(upload_to='images/400px/', null=True, blank=True)
    value = models.IntegerField(default=0, validators=[MinValueValidator(300), MaxValueValidator(30000)])
    temporary_image = models.ImageField(upload_to='temporary_images/', null=True, blank=True)
    expiration_time = models.DurationField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.temporary_image and not self.expiration_time:
            self.expiration_time = timezone.timedelta(seconds=self.value)
        super().save(*args, **kwargs)


###########################################################
######### Changing the resolution of a saved image ########
###########################################################
@receiver(pre_save, sender=Images)
def resize_images(sender, instance, **kwargs):
    if instance.image:
        image = Image.open(instance.image)
        
        image_200px = resize_image(image, (200, 200), instance.image.name)
        instance.image_200px = image_200px

        image_400px = resize_image(image, (400, 400), instance.image.name)
        instance.image_400px = image_400px

###########################################################
###### Auxiliary function to change image resolution ######
###########################################################
def resize_image(image, size, filename):
    img = image.copy()
    img.thumbnail(size)

    output = BytesIO()
    img.save(output, format='JPEG')
    output.seek(0)

    return InMemoryUploadedFile(output, 'ImageField', f"{filename.split('.')[0]}_resized.jpg", 'image/jpeg', output.getbuffer().nbytes, None)

