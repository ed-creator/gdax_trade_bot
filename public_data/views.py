from django.shortcuts import render

# Create your views here.
def pair_list(request):
    return render(request, 'public_data/pair_list.html', {})
