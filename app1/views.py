from django.shortcuts import render

# Create your views here.
def v1_app1(request):
    return render(request, 'app1/v1_app1.html')

def v2_app1(request):
    return render(request, 'app1/v2_app1.html')