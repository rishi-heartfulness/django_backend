from django.http import HttpResponse

def root(request):
     response =  "please register to access the products api"
     return HttpResponse(response)

     