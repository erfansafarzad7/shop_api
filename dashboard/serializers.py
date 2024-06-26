from rest_framework import serializers
from dashboard.models import Dashboard


class DashboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dashboard
        fields = ('user', 'first_name', 'last_name', 'address', 'state', 'city', 'postalcode')
        depth = 2
