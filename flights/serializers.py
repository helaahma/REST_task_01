from rest_framework import serializers
from .models import Flight, Booking

class FlightsSerializers(serializers.ModelSerializer):
	class Meta:
		model=Flight
		exclude=["miles"]

class BookingSerializers(serializers.ModelSerializer):
	class Meta:
		model= Booking
		fields=["flight", "date", "id"]