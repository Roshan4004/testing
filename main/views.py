from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import alldata
import json
from django.core.serializers import serialize

# Create your views here.

def home(request):
    context={}
    all= alldata.objects.all()

    intense=all.order_by("-intensity").values().exclude(intensity= None)
    relevant=all.order_by("-relevance").values().exclude(intensity= None)
    likely=all.order_by("-likelihood").values().exclude(intensity= None)
    context["ordered"]={"intense":intense,"relevant":relevant,"likely":likely}

    context["alldata"]=all

    pie_sector=[[],[]]
    ok=alldata.objects.values_list("sector",flat=True)
    for i in ok:
        if not i == "":
            if i in pie_sector[0]:
                index=pie_sector[0].index(i)
                pie_sector[1][index]=pie_sector[1][index]+1
            else:
                pie_sector[0].append(i)
                pie_sector[1].append(1)
    context["pie_data"]=pie_sector
    total={}
    filter_option={}
    for i in ["sector","region","country","source","topic","pestle"]:
        number=set(alldata.objects.values_list(i,flat=True))
        number.remove("")
        total[i]=len(number)
        filter_option[i]=list(number)
    context["total"]=total
    context["filter_option"]=filter_option
    # print(context)
    return render(request,'home2.html',{'all':context})

import ast
from django.core import serializers 
from django.db.models import Q
def filter_all(request):
    ok=alldata.objects.all()
    if is_ajax(request=request) and request.method=="GET":
        data_of=request.GET.get("final")
        my_dict = ast.literal_eval(data_of)
        if my_dict["pestle"]!=[]:
                for j in my_dict["pestle"]:
                    ok=ok.filter(pestle=j)
        if my_dict["source"]!=[]:
                for j in my_dict["source"]:
                    ok=ok.filter(source=j)
        if my_dict["topic"]!=[]:
                for j in my_dict["topic"]:
                    ok=ok.filter(topic=j)
        if my_dict["sector"]!=[]:
                for j in my_dict["sector"]:
                    ok=ok.filter(sector=j)
        if my_dict["region"]!=[]:
                for j in my_dict["region"]:
                    ok=ok.filter(region=j)
        # print(my_dict["end_year"])
        if my_dict["end_year"] != "" and my_dict["end_year"] != 0:
            ok=ok.filter(end_year__lte=int(my_dict["end_year"]))
        ok=serializers.serialize('json', ok)
        context={"msg":"success","alldata":ok}
        return JsonResponse(context)
    else:
        query_filters=request.POST.get("query_filters")
        search_param=request.POST.get("search_param")
        ok=alldata.objects.all()
        if ast.literal_eval(query_filters) != "":
            my_dict = ast.literal_eval(query_filters)
            if my_dict["pestle"]!=[]:
                    for j in my_dict["pestle"]:
                        ok=ok.filter(pestle=j)
            if my_dict["source"]!=[]:
                    for j in my_dict["source"]:
                        ok=ok.filter(source=j)
            if my_dict["topic"]!=[]:
                    for j in my_dict["topic"]:
                        ok=ok.filter(topic=j)
            if my_dict["sector"]!=[]:
                    for j in my_dict["sector"]:
                        ok=ok.filter(sector=j)
            if my_dict["region"]!=[]:
                    for j in my_dict["region"]:
                        ok=ok.filter(region=j)
            if my_dict["end_year"] != "" and my_dict["end_year"] != 0:
                ok=ok.filter(end_year__lte=int(my_dict["end_year"]))
        ok=ok.filter(Q(title__icontains=search_param) | Q(insight__icontains=search_param) | Q(source__icontains=search_param))
        ok=serializers.serialize('json', ok)
        context={"msg":"success","alldata":ok}
        return JsonResponse(context)

def individual_data(request):
    pk=request.GET.get("pk")
    if pk is not None and pk != "":
        ok=alldata.objects.filter(pk=pk)
        return render(request,'individual.html',{'ok':ok})
    else:
         return HttpResponse("Wrong ID")

def pie_data(request):
    if is_ajax(request=request):
        data_of=request.GET.get("data")
        all=[[],[]]
        ok=alldata.objects.values_list(data_of,flat=True)
        for i in ok:
            if not i == "":
                if i in all[0]:
                    index=all[0].index(i)
                    all[1][index]=all[1][index]+1
                else:
                    all[0].append(i)
                    all[1].append(1)
        context={"msg":"success","label":all[0],"data":all[1]}
        return JsonResponse(context)

def orderd_list(request):
    if is_ajax(request=request):
        data_of=request.GET.get("data")
        all=[[],[]]
        ok=alldata.objects.values_list(data_of,flat=True)
        for i in ok:
            if not i == "":
                if i in all[0]:
                    index=all[0].index(i)
                    all[1][index]=all[1][index]+1
                else:
                    all[0].append(i)
                    all[1].append(1)
        context={"msg":"success","label":all[0],"data":all[1]}
        return JsonResponse(context)

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

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
