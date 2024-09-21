# SimpleGismeteoParser
Скрипт вытягивает данные по текущей погоде с Gismeteo. \
Установка зависимостей: \
`$ sudo pip3 install -r requirements.txt` \
Запуск: 
```
$ ./parser.py --help
usage: parser.py [-h] [-j] [url]

Parse weather data from Gismeteo.

positional arguments:
  url         URL of the weather page, https://www.gismeteo.ru/weather-bryansk-4258/now/ by default

optional arguments:
  -h, --help  show this help message and exit
  -j, --json  Output in JSON format
```
Примеры вывода: 
```
Температура воздуха: +16,8°C
Скорость ветра: 2 м/с
Давление: 743 мм рт. ст.
```

```
{
  "temperature": "13°C",
  "wind_speed": "2 м/с",
  "pressure": "746 мм рт. ст."
}
```
