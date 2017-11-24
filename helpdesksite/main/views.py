from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home(request):
#    return HttpResponse('Landing page for main')

def home(request):
    item_name = "laptop"
    amount = "1,200.00"
    context = {'item_name': item_name,
                'amount': amount}
    return render(request, 'index.html', context)
