import requests
import os
from dotenv import load_dotenv

# Load the secret key from the .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_outfit_suggestion(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        # 'weather' is a list, we want the first item's 'main' status (e.g., Rain, Clouds, Clear)
        condition = data['weather'][0]['main']
        wind_speed = data['wind']['speed']
        
        print(f"\n--- Weather Report for {city} ---")
        print(f"Condition: {condition}")
        print(f"Temp: {temp}°F | Wind: {wind_speed} mph")

        # Smart Outfit Logic
        suggestions = []

        # 1. Temperature Base
        if temp < 45:
            suggestions.append("Wear a heavy winter coat")
        elif temp < 65:
            suggestions.append("A light jacket or sweater is perfect")
        else:
            suggestions.append("T-shirt weather!")

        # 2. Condition-based additions
        if condition == "Rain":
            suggestions.append("Don't forget an umbrella and waterproof shoes")
        elif condition == "Snow":
            suggestions.append("Wear boots with good grip!")
        elif condition == "Clear" and temp > 70:
            suggestions.append("Grab your sunglasses 🕶️")

        # 3. Wind-based additions
        if wind_speed > 15:
            suggestions.append("It's windy! Avoid loose hats or thin scarves")

        return " | ".join(suggestions)
    else:
        return f"Error {response.status_code}: {response.json().get('message')}"

while True:
    city_input = input("\nEnter a city (or type 'quit' to exit): ").strip()
    
    if city_input.lower() == 'quit':
        print("Goodbye!")
        break
    
    if not city_input:
        print("Please enter a valid city name.")
        continue
        
    print(get_outfit_suggestion(city_input))