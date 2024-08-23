from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Soildata
from .forms import DataForm
from .serializers import SoildataSerializer

def soildata_view(request):
    soildata = Soildata.objects.all()
    return render(request, 'index.html', {"soildata": soildata})

def form_view(request):
    form = DataForm()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('soildata_view')
    context = {"form": form}
    return render(request, 'form.html', context)

class ListView(generics.ListCreateAPIView):
    queryset = Soildata.objects.all()
    serializer_class = SoildataSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soildata.objects.all()
    serializer_class = SoildataSerializer
