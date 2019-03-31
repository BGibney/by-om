from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from byom_cbv.models import Biome

class BiomeList(ListView):
    model = Biome

class BiomeCreate(CreateView):
    model = Biome
    fields = ['BIOME_NAME', 'SOIL_PH_MIN', 'SOIL_PH_MAX']
    success_url = reverse_lazy('byom_cbv:biome_list')

class BiomeUpdate(UpdateView):
    model = Biome
    fields = ['BIOME_NAME', 'SOIL_PH_MIN', 'SOIL_PH_MAX']
    success_url = reverse_lazy('byom_cbv:biome_list')

class BiomeDelete(DeleteView):
    model = Biome
    success_url = reverse_lazy('byom_cbv:biome_list')