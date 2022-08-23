from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import 

from .models import BurnInfo, BurnPic

class BurnInfoSerializer(ModelSerializer):
    
    class Meta:
        model = BurnInfo
        fields = '__all__'

'''
class BurnPicSerializer(ModelSerializer):
    class Meta:
        model = BurnPic
        fields = '__all__'
        
        def get_photo_url(self, burnpic):
        	request = self.context.get('request')
        	photo = burnpic.photo.url
        	return request.build_absolute_uri(photo)
'''

class BurnPicSerializer(ModelSerializer):
    photo = serializers.ImageField(use_url = False)
    class Meta:
        model = BurnPic
        fields = '__all__'