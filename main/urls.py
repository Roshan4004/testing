from django.urls import path
from main import views

urlpatterns = [
    path('',views.home,name="home"),
    path('intensity',views.intensity,name="intensity"),
    path('likelihood',views.likelihood,name="likelihood"),
    path('relevance',views.relevance,name="relevance"),
    path('pie_data',views.pie_data,name="pie_data")

    
]