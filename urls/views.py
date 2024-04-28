from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import UrlSerializer
import hashlib
from .models import Url

@api_view(['POST'])
def add(request):
    print(request.META['HTTP_HOST'])
    if 'long_url' not in request.data:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    request.data['key']=str(hex(int(hashlib.sha256(request.data['long_url'].encode('utf-8')).hexdigest(), 16) % 10**15))[2:]
    request.data['short_url']="http://"+request.META['HTTP_HOST']+"/"+request.data['key']


    serializer=UrlSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data,status=status.HTTP_201_CREATED)
    
def redirect(request,key):
    try:
        url=Url.objects.get(key=key)
    except Url.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return render(request,'redirect.html',context={'long_url':url.long_url})

@api_view(['DELETE'])
def delete(request):
    try:
        url=Url.objects.get(key=request.data['key'])
        url.delete()
        return Response(status=status.HTTP_200_OK)
    except Url.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET']) 
def get(request):
    if 'key' in request.data:
        try:
            url=Url.objects.get(key=request.data['key'])
        except Url.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(UrlSerializer(url).data,status=status.HTTP_302_FOUND)
    elif 'long_url'in request.data:
        try:
            url=Url.objects.get(long_url=request.data['long_url'])
        except Url.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(UrlSerializer(url).data,status=status.HTTP_302_FOUND)
    elif 'short_url'in request.data:
        try:
            url=Url.objects.get(short_url=request.data['short_url'])
        except Url.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(UrlSerializer(url).data,status=status.HTTP_302_FOUND)
    else:
        return  Response(status=status.HTTP_400_BAD_REQUEST)