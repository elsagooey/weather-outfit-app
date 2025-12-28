import requests
import os
from dotenv import load_dotenv

# Load the secret key from the .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_outfit_suggestion(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    
    response = requests.get(url)
    
    # Debugging
    print(f"DEBUG: Status {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        return f"In {city}, it's {temp}°F. Wear a jacket!"
    elif response.status_code == 401:
        return "Error 401: Your API key is either wrong or still 'waking up'. Wait 30 mins!"
    else:
        return f"Error {response.status_code}: {response.json().get('message')}"

city_input = input("Enter a city: ")
print(get_outfit_suggestion(city_input))