from django.shortcuts import render
from django.http.response import JsonResponse
from . models import Guest, Movie, Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import  APIView
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer
from django.http import Http404
from rest_framework import mixins, generics, viewsets, status
from django_filters.rest_framework import DjangoFilterBackend




# Create your views here.

# tari9a  lawla
def no_rest_no_model(request):
    guest=[
        {
            'id':1,
            'name':"lhoussaine hssini",
            'mobile':133626782
        },
        {
            'id': 2,
            'name': "lhoussaine hasnawi",
            'mobile': 85347578
        }
    ]
    return JsonResponse(guest, safe=False)

# tari9a  tanya
def no_rest_from_model(request):
    data=Guest.objects.all()
    response ={
        'guest':list(data.values('name', 'mobile'))
    }
    return JsonResponse(response)

# tari9a  talta
@api_view(['GET', 'POST'])
def   FBV_list(request):
        """
        List all code guest, or create a new guest.
        """
        if request.method == 'GET':
            guest = Guest.objects.all()
            serializer = GuestSerializer(guest, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = GuestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def FBV_detail(request, pk):
    """
    Retrieve, update or delete a code guest.
    """
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# tari9a  rab3a:::CBV Class based views

class CBV_list(APIView):
    """
    List all guest, or create a new guest.
    """
    def get(self, request, format=None):
        guest = Guest.objects.all()
        serializer = GuestSerializer(guest, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CBV_detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# tari9a  khamsa :::mixins list
class GuestList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class GuestDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request,pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

# tari9a  sadisa ::: Generics method

class GtList(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

# tari9a  sab7a ::: Viewset
class GuestViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backend=[DjangoFilterBackend]
    search_fields=['movie']

class ReservationsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


# tari9a  talta
@api_view(['GET'])
def   findmovie(request):
    movie = Movie.objects.filter(
        hall=request.data['hall'],
        movie=request.data['movie']
    )
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def   addreservation(request):
        movie = Movie.objects.get(
                hall=request.data['hall'],
                movie=request.data['movie'],
            )
        guest=Guest()
        guest.name=request.data['name']
        guest.mobile=request.data['mobile']
        guest.save()
        reservation=Reservation()
        reservation.guest=guest
        reservation.movie=movie
        reservation.save()
        return Response(status.HTTP_201_CREATED)