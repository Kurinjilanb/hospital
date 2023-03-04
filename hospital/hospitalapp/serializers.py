from . import models


class HospitalSerializer(serializers.ModelSerializer):
    """
    Serializer for Hospital model

    """

    class Meta:
        model = models.Hospital
        fields = '__all__'
