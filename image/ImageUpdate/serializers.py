from rest_framework import serializers
from .models import Images, UserProfile


###########################################################
## Defining fields of the Images model for adding images ##
###########################################################
class ImagesSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Images
        fields = ('id', 'title', 'image', 'image_200px', 'image_400px', 'temporary_image', 'value', 'user')


    def get_user(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return request.user.username
        return None
    
    def get_temporary_image(self, obj):
        if obj.temporary_image:
            request = self.context.get('request')
            temporary_image_url = obj.temporary_image.url
            if request is not None:
                return request.build_absolute_uri(temporary_image_url)
            return temporary_image_url
        return None


###########################################################
###### Defining the fields of the UserProfile model #######
###########################################################
class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'user_type')


###########################################################
# Definition of Images model fields to display all images #
###########################################################
class ImageURLSerializers(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Images
        fields = ('image_url',)


    def get_image_url(self, obj):
        request = self.context.get('request')
        user = request.user
        image_url = obj.image.url

        if user.userprofile.user_type == 'basic':
            return request.build_absolute_uri(obj.image_200px.url)
        elif user.userprofile.user_type == 'premium':
            return {
                'image_200px': request.build_absolute_uri(obj.image_200px.url),
                'image_400px': request.build_absolute_uri(obj.image_400px.url),
                'image': request.build_absolute_uri(obj.image.url)
            }
        elif user.userprofile.user_type == 'enterprise':
            return {
                'image_200px': request.build_absolute_uri(obj.image_200px.url),
                'image_400px': request.build_absolute_uri(obj.image_400px.url),
                'image': request.build_absolute_uri(obj.image.url),
                'temporary_image': None
            }
        
        return image_url