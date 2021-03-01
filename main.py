import os
import math
import csv
import requests
from bs4 import BeautifulSoup
from save_csv import save_to_csv
from extract_brand_alba import get_brand_albas_page, get_brand_alba_info

os.system("clear")
alba_url = "http://www.alba.co.kr"
request = requests.get(alba_url).text
html = BeautifulSoup(request,"html.parser")
brand_list = html.find(id="MainSuperBrand").find_all("li",{"class":"impact"})
for item in brand_list:
    brand_info = item.find("a",{"class":"goodsBox-info"})
    brand_link = brand_info['href']
    brand_name = brand_info.find("span",{"class":"company"}).text
    brand_alba_info = get_brand_albas_page(brand_link,brand_name)
    if brand_alba_info is not None:
        save_to_csv(brand_alba_info,brand_name)
  



