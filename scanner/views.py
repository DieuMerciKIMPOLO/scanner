from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

import time
from zapv2 import ZAPv2
import requests
import json

@api_view(['POST'])
def spider(request):
    if request.method == 'POST':
        apiKey = 'm2a58n594fjhsaliofsmjtas77'
        serverUrl = "http://localhost:8080"
        data   = request.data
        target = data['url']
        zap = ZAPv2(apikey=apiKey)
        scanID = zap.spider.scan(target)
        while int(zap.spider.status(scanID)) < 100:
            time.sleep(1)

        payload = {'apikey': apiKey, 'scanId': scanID}
        req = requests.get(serverUrl+'/JSON/spider/view/fullResults/', params=payload)
        response = json.loads(req.text)
        
        return Response(response)
    return Response({"error": "Bad request type"})

@api_view(['POST'])
def ajaxspider(request):
    if request.method == 'POST':

        apiKey = 'm2a58n594fjhsaliofsmjtas77'
        serverUrl = "http://localhost:8080"
        data   = request.data
        target = data['url']

        zap = ZAPv2(apikey=apiKey)
        scanID = zap.ajaxSpider.scan(target)
        timeout = time.time() + 60*2 

        while zap.ajaxSpider.status == 'running':
            if time.time() > timeout:
                break
            time.sleep(2)

        payload = {'apikey': apiKey, 'scanId': scanID}
        req = requests.get(serverUrl+'/JSON/ajaxSpider/view/fullResults/', params=payload)
        response = json.loads(req.text)
        
        return Response(response)
    return Response({"error": "Bad request type"})







