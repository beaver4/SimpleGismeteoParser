#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import requests
from bs4 import BeautifulSoup

if len (sys.argv) == 2:
    URL = sys.argv[1]
else:
    URL = 'https://www.gismeteo.ru/weather-bryansk-4258/now/'
    
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'}
BLUE = '\033[96m'
ENDC = '\033[0m'

response = requests.get(URL, headers=headers)
contents = response.text
soup = BeautifulSoup(contents, 'lxml')

 
temperature_now = soup.find("span", attrs={ "class" : "unit unit_temperature_c"}).text.strip() 
#temperature_value_m_element = soup.find("span", attrs={ "class" : "tab-weather__value_m"})
#if not temperature_value_m_element is None:
#    temperature_now = temperature_now + temperature_value_m_element.text.strip()

now_info_element = soup.find("div", attrs={ "class" : "now-info"})

wind_element = now_info_element.find("div", attrs={ "class" : "unit unit_wind_m_s"})
wind_speed = wind_element.find(text=True, recursive=False).strip()
wind_direction = wind_element.find("div", attrs={ "class" : "item-measure"}).text.replace("м/c", "").strip()

pressure = now_info_element.find("div", attrs={ "class" : "unit unit_pressure_mm_hg_atm"}).text.replace("ммрт. ст.", "").strip()

#humidity = now_info_element.find("div", attrs={ "class" : "nowinfo__item nowinfo__item_humidity"}).text.replace("Влажность", "").replace("%", "").strip()

#magnetic = now_info_element.find("div", attrs={ "class" : "nowinfo__item nowinfo__item_gm"}).find("div", attrs={ "class" : "nowinfo__value"}).text

#temperature_water_element = now_info_element.find("div", attrs={ "class" : "nowinfo__item nowinfo__item_water"})
#temperature_water = temperature_water_element.find("div", attrs={ "class" : "unit unit_temperature_c"}).text.replace("°C", "")

print(BLUE + "Температура воздуха: " + ENDC + temperature_now + "°C")
print(BLUE + "Ветер: " + ENDC + wind_speed + " м/с " + wind_direction)
print(BLUE + "Давление: " + ENDC + pressure + " мм рт. ст.")
#print("Влажность: " + humidity + "%")
#print("Г/м активность: " + magnetic + " баллов")
#print("Температура воды: " + temperature_water + "°C")


