from django.shortcuts import render
from .models import alldata

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
    
    context["all"]=all
    # print(context)
    average_data("intensity")
    return render(request,'home.html',context)

def average_data(pk):
    context={pk:{"averages":{}}}
    sort_by=["country","sector","region"]
    for data in sort_by:
        context[pk]["averages"][data]=[[],[]]
        all=set(alldata.objects.values_list(data,flat=True))
        all.remove("")
        for i in all:
            i_occurs=len(alldata.objects.filter(data=i))
            avg_intensity_i=len(set(alldata.objects.filter(region=i).values_list(pk,flat=True)))/i_occurs
            # context["intensity"]["averages"]["region"]=[[],[]]
            context["intensity"]["averages"][data][0].append(i)
            context["intensity"]["averages"][data][1].append(avg_intensity_i)
    print(context)
    return None