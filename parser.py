#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import requests
from bs4 import BeautifulSoup

if len (sys.argv) == 2:
    URL = sys.argv[1]
else:
    URL = 'https://www.gismeteo.ru/weather-bryansk-4258/now/'
    
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}

response = requests.get(URL, headers=headers)
contents = response.text
soup = BeautifulSoup(contents, 'lxml')

 
temperature_now = soup.find("span", attrs={ "class" : "js_value tab-weather__value_l"}).text.strip() 
#temperature_value_m_element = soup.find("span", attrs={ "class" : "tab-weather__value_m"})
#if not temperature_value_m_element is None:
#    temperature_now = temperature_now + temperature_value_m_element.text.strip()

now_info_element = soup.find("div", attrs={ "class" : "now__info nowinfo"})

wind_element = now_info_element.find("div", attrs={ "class" : "unit unit_wind_m_s"})
wind_speed = wind_element.find("div", attrs={ "class" : "nowinfo__value"}).text.strip()
wind_direction = wind_element.find("div", attrs={ "class" : "nowinfo__measure nowinfo__measure_wind"}).text.replace("м/с", "").strip()

pressure = now_info_element.find("div", attrs={ "class" : "unit unit_pressure_mm_hg_atm"}).text.replace("мм рт. ст.", "").strip()

humidity = now_info_element.find("div", attrs={ "class" : "nowinfo__item nowinfo__item_humidity"}).text.replace("Влажность", "").replace("%", "").strip()

magnetic = now_info_element.find("div", attrs={ "class" : "nowinfo__item nowinfo__item_gm"}).find("div", attrs={ "class" : "nowinfo__value"}).text

temperature_water_element = now_info_element.find("div", attrs={ "class" : "nowinfo__item nowinfo__item_water"})
temperature_water = temperature_water_element.find("div", attrs={ "class" : "unit unit_temperature_c"}).text.replace("°C", "")

print("Температура воздуха: " + temperature_now + "°C")
print("Ветер: " + wind_speed + " м/с " + wind_direction)
print("Давление: " + pressure + " мм рт. ст.")
#print("Влажность: " + humidity + "%")
#print("Г/м активность: " + magnetic + " баллов")
#print("Температура воды: " + temperature_water + "°C")


