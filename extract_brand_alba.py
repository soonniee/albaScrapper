import os
import math
import csv
import requests
from bs4 import BeautifulSoup
from save_csv import save_to_csv
def get_brand_alba_info(html):
    brand_albas = html.find(id="NormalInfo").find("tbody").find_all("tr",{"class":""})
    # brand_albas = brand_albas[::2]
    brand_albas_info_pagination=[]
    for alba in brand_albas:
        alba_dict={}
        alba_place = alba.find("td",{"class","local"}).text.replace(u'\xa0', ' ')
        alba_title = alba.find("td",{"class","title"}).find("span",{"class":"company"}).text.strip()
        alba_time = alba.find("td",{"class","data"}).text.replace(u'\xa0', ' ')
        alba_pay = alba.find("td",{"class","pay"}).text.replace(u'\xa0', ' ')
        alba_date = alba.find("td",{"class","regDate"}).text.replace(u'\xa0', ' ')
        alba_dict = {'place':alba_place,
                    'title':alba_title, 
                    'time':alba_time, 
                    'pay':alba_pay, 
                    'date':alba_date }
        brand_albas_info_pagination.append(alba_dict)
    return brand_albas_info_pagination  
def get_brand_albas_page(brand_link,brand_name):
    brand_url = f"{brand_link}job/brand"
    print(brand_url)
    try:
        request = requests.get(brand_url).text
        html = BeautifulSoup(request,"html.parser")
        paging = html.find("p",{"class":"jobCount"}).find("strong").text
        paging = paging.replace(',','')
        paging = int(paging)
        last_page = math.ceil(paging / 50)
        brand_albas_info_all=[]
        for i in range(last_page):
            print(f"Extract {brand_name}'s albas : Page{i+1}...")
            pagination_url = f"{brand_link}/?page={i+1}"
            request = requests.get(brand_url).text
            pagination_html = BeautifulSoup(request,"html.parser")
            info_pagination = get_brand_alba_info(pagination_html)
            brand_albas_info_all.extend(info_pagination)
        return brand_albas_info_all
    except:
        print(f"There is no brand({brand_name}) page")
   