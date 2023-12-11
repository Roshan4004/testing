import json
from datetime import datetime
# with open("jsondata.json", "r") as lst:
# lst = open("jsondata.json ", "r").readlines()
# print(lst)
null_list=["end_year","intensity","start_year","impact","relevance","likelihood"]
final=[]
a=1
file = open("jsondata.json",encoding='utf-8-sig')
ok=file.read()
okk=json.loads(ok)
for i in okk:
    if i["added"] == "":
        i["added"] = None
    else:
        added=i["added"]
        i["added"]=str(datetime.strptime(added, "%B, %d %Y %H:%M:%S"))
    if i["published"]== "":
        i["published"]= None
    else:
        pub=i["published"]
        i["published"]=str(datetime.strptime(pub, "%B, %d %Y %H:%M:%S"))

    for gg in null_list:
        if i[gg]=="":
            i[gg]= None
    new={
        "model":"main.alldata",
        "pk":a,
        "fields":i
        }
    a+=1
    final.append(new)
    
# print(final)
with open('final.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=4)

# main=open('jsondata.json')
# print(main[1])
# json_object = json.dumps(main)
# jj=json.loads(json_object)
# print(jj)

# json_formatted_str = json.dumps(json_object, indent=2)

# print(json_formatted_str)
# print(json.dumps(main))

# object_to_be_saved={}
# with open("jsondata.json", "r") as json_file:
#     json.load(json_file)

# print(object_to_be_saved)