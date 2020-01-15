from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from . models import EventRegistration
from .serializer import EventSerializer,UserSerializer,AccountSeliazier
from rest_framework import generics
from django.contrib.auth import authenticate
from  rest_framework import status
#from rest_framework.permissions import IsAuthenticated
#from rest_framework import permissions
from django.http import Http404

class Eventlist(APIView):

    def get(self,request):
        maxdata=20
       # pools=EventRegistration.objects.all()[:20]   #only 20 recoreds displayed
        pools = EventRegistration.objects.all()[:maxdata]
        data=EventSerializer(pools,many=True).data
        return Response(data)

class EventDetails(APIView):
    def get(self,request):
        global data
        poll=get_object_or_404(EventRegistration)
        data=EventSerializer(poll).data
        return Response(data)
class Usercreate_or_Registeruser(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
class LoginApi(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = ()
    def post(self,request,):
        username=request.data.get("username")
        password=request.data.get("password")
        user=authenticate(username=username,password=password)
        if user:
            return Response("login success")
        else:
            return Response({"error":"wrong credentials"},status=status.HTTP_400_BAD_REQUEST)
class AccountDelete(generics.DestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated)
    serializer_class = AccountSeliazier
    lookup_field = "email"
    queryset = EventRegistration.objects.all()
    def get(self,request):
        try:
            instance=self.queryset.get(email=self.request.user)
            return  instance
        except EventRegistration.DoesNotExist:
            raise Http404
