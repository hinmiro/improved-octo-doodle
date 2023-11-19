import requests


class Weather:

    def __init__(self, api, city):
        self.api = api
        self.city = city



class Forecast(Weather):

    def __init__(self, api, city):
        super().__init__(api, city)
        self.weather_forecast()

    def weather_forecast(self):
        request = f"https://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={self.api}&units=metric"
        data = requests.get(request).json()
        self.json_parser(data)

    def json_parser(self, data):
        data1 = data['list'][5]
        data2 = data['list'][13]
        data3 = data['list'][21]
        print(f":::{data['city']['name']}:::\n"
              f"\nTime: {data1['dt_txt']}\n"
              f"Temperature: {data1['main']['temp']} degrees of celsius, feels like {data1['main']['feels_like']}\n"
              f"Description: {data1['weather'][0]['description']}\n"
              f"\n")

        print(f"Time: {data2['dt_txt']}\n"
              f"Temperature: {data2['main']['temp']} degrees of celsius, feels like {data2['main']['feels_like']}\n"
              f"Description: {data2['weather'][0]['description']}\n"
              f"\n")

        print(f"Time: {data3['dt_txt']}\n"
              f"Temperature: {data3['main']['temp']} degrees of celsius, feels like {data3['main']['feels_like']}\n"
              f"Description: {data3['weather'][0]['description']}\n"
              f"\n")




class Nowcast(Weather):

    def __init__(self, api, city):
        super().__init__(api, city)
        self.weather_nowcast()

    def weather_nowcast(self):
        request = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api}&units=metric&lang=fi"
        data = requests.get(request)
        if data.status_code == 200:
            data = requests.get(request).json()
            self.json_parser(data)
        else:
            print(f"Error {data.status_code}")

    def json_parser(self, data):
        main = data['main']
        weather = data['weather']
        print(f":::Weather in {data['name']}:::\n"
              f"Temperature: {int(main['temp'])}, feels like: {main['feels_like']}\n"
              f"Description: {weather[0]['description']}")


# token = input("Type your openweather token here: ")
token = "76c97ac5f76c834bdfc72d531dfaa2b5"
run = True
print("Weather app, type X to city query for shutting down program")
while run:
    query = input("\nType city: ")
    if query.upper() == "X":
        break
    else:
        weather1 = Forecast(token, query)

