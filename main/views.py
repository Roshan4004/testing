from django.shortcuts import render
from .models import alldata
import json
from django.core.serializers import serialize

# Create your views here.

def home(request):
    context={"intensity":{"averages":{"sector":[[],[]],"region":[[],[]]}}}
    all= alldata.objects.all()

    all_sectors=set(alldata.objects.values_list('sector',flat=True))
    all_sectors.remove("")
    for sector in all_sectors:
        sector_occurs=len(alldata.objects.filter(sector=sector))
        avg_intensity_sector=len(set(alldata.objects.filter(sector=sector).values_list('intensity',flat=True)))/sector_occurs
        context["intensity"]["averages"]["sector"][0].append(sector)
        context["intensity"]["averages"]["sector"][1].append(avg_intensity_sector)
    # print(alldata.objects.filter(sector="Energy").values_list('intensity',flat=True))
    
    all_region=set(alldata.objects.values_list('region',flat=True))
    all_region.remove("")
    for region in all_region:
        region_occurs=len(alldata.objects.filter(region=region))
        avg_intensity_region=len(set(alldata.objects.filter(region=region).values_list('intensity',flat=True)))/region_occurs
        # context["intensity"]["averages"]["region"]=[[],[]]
        context["intensity"]["averages"]["region"][0].append(region)
        context["intensity"]["averages"]["region"][1].append(avg_intensity_region)

    context["intensity"]["averages"]["country"]=[[],[]]
    all_country=set(alldata.objects.values_list('country',flat=True))
    all_country.remove("")
    for country in all_country:
        country_occurs=len(alldata.objects.filter(country=country))
        avg_intensity_country=len(set(alldata.objects.filter(country=country).values_list('intensity',flat=True)))/country_occurs
        context["intensity"]["averages"]["country"][0].append(country)
        context["intensity"]["averages"]["country"][1].append(avg_intensity_country)
    
    context["all"]=serialize('json',all)
    # final={"everything":{context}}
    # print(context)
    print(avg_data("relevance"))
    return render(request,'home2.html',{'all':{json.dumps(context)}})

def intensity(request):
    context=avg_data("intensity")
    # print(context)
    return render(request,'intensity.html',context)

def likelihood(request):
    context=avg_data("likelihood")
    # print(context)
    return render(request,'likelihood.html',context)

def relevance(request):
    context=avg_data("relevance")
    # print(context)
    return render(request,'relevance.html',context)

def avg_data(ok):
    context={"averages":{}}

#Averge intensity by Sector
    context["averages"]["sector"]=[[],[]]
    all_sectors=set(alldata.objects.values_list('sector',flat=True))
    all_sectors.remove("")
    for sector in all_sectors:
        sector_occurs=len(alldata.objects.filter(sector=sector))
        avg_intensity_sector=len(set(alldata.objects.filter(sector=sector).values_list(ok,flat=True)))/sector_occurs
        context["averages"]["sector"][0].append(sector)
        context["averages"]["sector"][1].append(avg_intensity_sector)

#Averge intensity by region
    context["averages"]["region"]=[[],[]]
    all_region=set(alldata.objects.values_list('region',flat=True))
    all_region.remove("")
    for region in all_region:
        region_occurs=len(alldata.objects.filter(region=region))
        avg_intensity_region=len(set(alldata.objects.filter(region=region).values_list(ok,flat=True)))/region_occurs
        # context["intensity"]["averages"]["region"]=[[],[]]
        context["averages"]["region"][0].append(region)
        context["averages"]["region"][1].append(avg_intensity_region)

#Averge intensity by Country
    context["averages"]["country"]=[[],[]]
    all_country=set(alldata.objects.values_list('country',flat=True))
    all_country.remove("")
    for country in all_country:
        country_occurs=len(alldata.objects.filter(country=country))
        avg_intensity_country=len(set(alldata.objects.filter(country=country).values_list(ok,flat=True)))/country_occurs
        context["averages"]["country"][0].append(country)
        context["averages"]["country"][1].append(avg_intensity_country)
    return context