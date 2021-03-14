from django.urls import path
from .views import OccDetailView

urlpatterns = [
    path('detail/<int:pk>/', OccDetailView.as_view(), name='occ_detail'),
]
