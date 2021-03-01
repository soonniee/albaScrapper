import csv

def save_to_csv(brand_albas_info,brand_name):
    brand_name = brand_name.replace('/','_')
    file = open(f"C:/Users/Sun/Desktop/python/albaScrapper/csv/{brand_name}.csv","w",-1,"utf-8")
    writer = csv.writer(file)
    writer.writerow(["place ,title, time, pay, date"])
    for alba_info in brand_albas_info:
        writer.writerow(list(alba_info.values()))
    return