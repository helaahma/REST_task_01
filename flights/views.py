from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightsSerializers, BookingSerializers
from datetime import date

class FlightList(ListAPIView):
	queryset= Flight.objects.all()
	serializer_class = FlightsSerializers

class BookingList(ListAPIView):
	queryset= Booking.objects.filter(date__gt=date.today())
	serializer_class = BookingSerializers

