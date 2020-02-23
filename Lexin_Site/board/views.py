from django.shortcuts import render

# Create your views here.
def kepu(request):
    return render(request, 'kepu.html')



def news(request):
    return render(request, 'news.html')