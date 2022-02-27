import json
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.urls.conf import path
from .thirdparty import juhe


def index(request):
    return HttpResponse('你好,世界,china！')


def arff(request):
    return HttpResponse("arff")

# def hellworld(request):
# 	print('request method:',request.method)
# 	print('request.META',request.META)
# 	print('request cookies',request.COOKIES)
# 	print('request QueryDict:',request.GET)
# 	# return HttpResponse(content='OK',status=520)
# 	m={
# 		"message":"Hello Django Response"
# 	}
# 	return JsonResponse(data=m,safe=False,status=200)
# 	pass


def weather(request):
    if request.method == 'GET':
        data = []
        city = request.GET.get('city')
        result = juhe.main(city)
        result['city_info'] = city
        data.append(result)
        return JsonResponse(data=data, safe=False, status=200)
    elif request.method == 'POST':
        re = request.body.decode('utf-8')
        re_body = json.loads(re)
        cities = re_body.get('city')
        data = []
        for city in cities:
            result = juhe.main(city)
            result['city_info'] = city
            data.append(result)
        return JsonResponse(data=data, safe=False, status=200)
