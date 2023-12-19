from django.urls import path
from main import views

urlpatterns = [
    path('',views.home,name="home"),
    path('intensity',views.intensity,name="intensity"),
    path('likelihood',views.likelihood,name="likelihood"),
    path('relevance',views.relevance,name="relevance"),
    path('pie_data',views.pie_data,name="pie_data"),
    path('filter_all',views.filter_all,name="filter_all"),
    path('individual_data',views.individual_data,name="individual_data")

    
]