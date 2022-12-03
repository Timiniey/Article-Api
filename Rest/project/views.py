from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from . serializers import ArticleSerializer
from . models import Article
from django.http import HttpResponse

@api_view(['GET'])
def getdata(request):
        article=Article.objects.all()
        serializer=ArticleSerializer(article,many=True)
        return Response(serializer.data)

@api_view (["GET"])
def getlist(request,pk):
        article=Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, many=False)
        return Response (serializer.data)
        
@api_view(['POST'])
def adddata(request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
@api_view (['DELETE'])
def deletedata(request,pk):
        article=Article.objects.get(pk=pk)
        article.delete()
        return HttpResponse("Successfully deleted")

@api_view (['POST'])
def updatedata(request, pk):
        article=Article.objects.get(pk=pk)
        serializer=ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response(serializer.data)
        return Response(serializer.data)
        
        

             
             
        

