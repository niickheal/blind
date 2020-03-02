from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Feed,Books
from . serializers import postSerializer

class postList(APIView):
	def get(self,request):
		allpost = Feed.objects.all()
		Feed.objects.filter(id=0).delete()
		serializer = postSerializer(allpost,many =True)
		return Response(serializer.data)

	def post(self):
		pass

class booksList(APIView):
    def get(self,request):
        allpost = Books.objects.all()
        Books.objects.filter(id=0).delete()
        serializer = postSerializer(allpost,many =True)
        return Response(serializer.data)

    def post(self):
        pass

