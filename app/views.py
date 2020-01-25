from django.http import HttpResponse

def home(request):
    return HttpResponse('my name is khan!')

