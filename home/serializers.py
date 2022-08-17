from rest_framework import serializers
from .models import *
class layToanBoDataJsonEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerDataEnglish
        fields = ('DataJson',)