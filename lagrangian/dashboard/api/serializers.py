from rest_framework.serializers import ModelSerializer
from dashboard.models import *
class DashboardSerializer(ModelSerializer):
    class Meta:
        model= DashboardPost
        fields=["title","file"]
        