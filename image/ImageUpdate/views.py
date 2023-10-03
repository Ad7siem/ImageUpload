from rest_framework import viewsets
from .models import Images, UserProfile
from .serializers import ImagesSerializers, UserProfileSerializers, ImageURLSerializers


###########################################################
###### View of adding new images to the Images model ######
###########################################################
class ImagesView(viewsets.ModelViewSet):
    serializer_class = ImagesSerializers

    def get_queryset(self):
        user = self.request.user
        return Images.objects.filter(user=user)
        
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


###########################################################
## View of setting the user type in the UserProfile model #
###########################################################
class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


###########################################################
######### View displaying all images for the user #########
###########################################################
class UserImagesView(viewsets.ModelViewSet):
    serializer_class = ImageURLSerializers
    
    def get_queryset(self):
        user = self.request.user
        user_profile = UserProfile.objects.get(user=user)
        return Images.objects.filter(user=user)



