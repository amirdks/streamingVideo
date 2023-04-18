from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index_view"),
    # path('media/<path>', views.Aha.as_view(), name="aha_view"),
]
