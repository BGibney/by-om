from django.urls import path

from . import views

app_name = 'byom_cbv'

urlpatterns = [
  path('', views.BiomeList.as_view(), name='biome_list'),
  path('new', views.BiomeCreate.as_view(), name='biome_new'),
  path('edit/<int:pk>', views.BiomeUpdate.as_view(), name='biome_edit'),
  path('delete/<int:pk>', views.BiomeDelete.as_view(), name='biome_delete'),
]