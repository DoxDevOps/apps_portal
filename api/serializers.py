from rest_framework import serializers
from portal.models import App
class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ["name", "description", "url", "icon"]
        
   