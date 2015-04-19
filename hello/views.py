from django import http

def home(request):
    return http.HttpResponse('Hello App Engine and Django World!')
    return http.HttpResponse('Pleased to meet you!')
