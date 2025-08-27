import requests

def get_weather(city):
    api_key="your api key"
    #replace with your openweather api key 
    base_url="https://api.openweathermap.org/data/2.5/weather"
    params={
        "q":city,
        "appid":api_key,
        "units":"metric"
        #for celsius
    }
    response=requests.get(base_url,params=params)
    if response.status_code==200:
        data=response.json()
        print(f"weather in {city}:\n")
        print(f"Temperature:{data['main']['temp']}C")
        print(f"Condition:{data['weather'][0]['description'].capitalize()}")
        print(f"Humidity:{data['main']['humidity']}%")
        print(f"Wind Speed:{data['wind']['speed']}m/s")
    else:
        print("City not found or error fetching data.")

cityname=input("Enter the city name: ")
get_weather(cityname)