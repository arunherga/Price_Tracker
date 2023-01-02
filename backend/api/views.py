import json
from django.shortcuts import render
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    # request->http req->django
    # request.body
    #print(dir(request))
    body = request.body # byte string of json data
    data = {}
    try:
        data = json.load(body)
    except:
        pass
    print(data.keys())
    print(body)
    data['headers']=request.headers
    data['content']=request.content_type
    print(data)
    print(request.headers)
    return JsonResponse({"Message":"Hi this is your Json API Response!!!"})
    
