import re
import json
# -*- coding: utf-8 -*-

#"""
#Cvičení 7. - práce s daty

#Vaším dnešním úkolem je spojit dohromady data, uložená ve dvou různých
#souborech. První soubor obsahuje výsledky závodu - jména a časy závodníků. Druhý
#pak obsahuje databázi závodníků uloženou jako JSON - mimo jiné jejich id. Cílem
#je vytvořit  program, který tyto data propojí, tedy ke každému závodníkovi ve
#štafetě najde jeho id. Případně také nenajde, data nejsou ideální. I tuto
#situaci ale musí program korektně ošetřit.  Výsledky programu bude potřeba
#zapsat do dvou souborů.

#Kompletní zadání je jako vždy na https://elearning.tul.cz/

#"""


def output_json(result_list):
    #"""
    #Uloží list slovníků do souboru output.json tak jak je požadováno 
    #v zadání.
    #"""
    with open('output.json', 'w') as output:
        output.write(json.dumps(result_list, indent=4, sort_keys=True))

def output_correct(result_list, path):
    w = open(path, "w", encoding='utf-8-sig')
    sorted_result_list=sorted(result_list, key=lambda d: d["id"])
    for r in sorted_result_list:
        s=str(r["id"])+" "+str(r["result"])+"\n"
        w.write(s)
    w.close()

def output_error(result_list, path):
    w = open(path, "w", encoding='utf-8-sig')
    for r in result_list:
        s=r["fullname"]+"\n"
        w.write(s)
    w.close()

def input_html(path):
    #uprava textu
    f=open(path)
    text=f.read()
    f.close()
    text=text.split("Relay</strong></p>")
    relays=text[1]
    relays=relays.replace("</p>", "")
    relays=relays.replace("</div>", "")
    relays=relays.replace("</body>", "")
    relays=relays.replace("</html>", "")
    relays=relays.replace("\n", "")
    relays=relays.replace(".", "")
    relays=relays.strip()
    strings=relays.split("<p>")
    #ukladani do listu dictionary
    html_list=[]
    for s in strings:
        s=s.strip()
        if (s.__eq__("Women")):
            gender="F"
        elif (s.__eq__("Men")):
            gender="M"
        else:
            results=re.split("\),", s)
            for r in results:
                if not (r.__eq__("")):
                    placement=re.search("\d+", r).group(0)
                    time=re.search("\d+:\d+:\d+", r).group(0)
                    names=re.findall("([a-zA-Z-]{1,}.[a-zA-Z-]{1,}\s[a-zA-Z-]{1,})", r)
                    #zbavuje se zemi s dvěma slovy (Czech Republic, United Kingdom)
                    if (names.__len__()==4):
                        names.pop(0)
                    name1=names[0].split(" ")
                    name2=names[1].split(" ")
                    name3=names[2].split(" ")
                    html_list.append(to_dict_html(placement, time, name1))
                    html_list.append(to_dict_html(placement, time, name2))
                    html_list.append(to_dict_html(placement, time, name3))
    #print(html_list)
    return html_list

def to_dict_html(p, t, n):
    person={}
    if (n.__len__()==3):
        f=n[0]+" "+n[1]+" "+n[2]
        person={
            "result": p,
            "time": t,
            "fullname": f
        }
    else:
        person={
            "result": p,
            "time": t,
            "firstname": n[0],
            "lastname": n[1]
        }
    return person

def input_json(path, html_data):
    with open(path, encoding="utf8") as json_file:
        data = json.load(json_file)
    json_output=[]
    txt_correct=[]
    txt_error=[]
    for person in html_data:
        if "fullname" in person.keys():
            d={
                "id": "False",
                "result": person["result"],
                "time": person["time"],
                "no_match": person["fullname"]
            }
            json_output.append(d)
            t={
                "fullname": person["fullname"]
            }
            txt_error.append(t)
        else:
            found=0
            for reg in data:
                if (person["firstname"]==reg["firstname"]) and (person["lastname"]==reg["lastname"]):
                    found=1
                    ID=reg["id"]
                    break
            if (found==1):
                d={
                    "id": ID,
                    "result": person["result"],
                    "time": person["time"]
                }
                json_output.append(d)
                t={
                    "id": ID,
                    "result": person["result"]
                }
                txt_correct.append(t)
            else:
                fullname=person["firstname"]+" "+person["lastname"]
                d={
                    "id": "False",
                    "result": person["result"],
                    "time": person["time"],
                    "no_match": fullname
                }
                json_output.append(d)
                t={
                    "fullname": fullname
                }
                txt_error.append(t)
    output_json(json_output)
    output_correct(txt_correct, "compare.txt")
    output_error(txt_error, "errors.txt")

if __name__ == '__main__':
    html_data=input_html("result.html")
    input_json("competitors.json", html_data)