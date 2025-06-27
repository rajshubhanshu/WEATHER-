import requests
API_KEY = "099ff028f6782addd517d9f6743aa0f3"  # <-- apni OpenWeatherMap API key yahan dalo

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"Weather in {city}: {temp}°C, {desc}")
    else:
        print(f"City not found or API error.status_code: {response.status_code}")
        print(response.json())

city = input("Enter city name: ")
get_weather(city)
