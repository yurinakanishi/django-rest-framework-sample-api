from rest_framework import serializers
from .models import LivingThings, Habitat, Species


class LivingThingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivingThings
        fields = "__all__"


class HabitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitat
        fields = "__all__"


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = "__all__"
