from django.http import HttpResponse

def index(request):
    return HttpResponse('helle')
def hello(request):
    return HttpResponse('woshihello')