import requests

def get_outfit_suggestion(city):
    api_key = "294c6fffebb7eb9238e49278005213c1" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    # Send the request
    response = requests.get(url)
    
    # --- DEBUG SECTION ---
    # This will print the raw status (like 401 or 200) and the message
    print(f"DEBUG: Status Code: {response.status_code}")
    print(f"DEBUG: Response JSON: {response.json()}")
    # ---------------------

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather = data['weather'][0]['main']
        
        print(f"\nThe temperature in {city} is {temp}°F with {weather}.")
        
        if temp < 50:
            return "Suggestion: Wear a heavy coat!"
        elif temp < 70:
            return "Suggestion: A light jacket or hoodie is fine."
        else:
            return "Suggestion: It's T-shirt weather!"
    else:
        return "The backend couldn't get the weather. Check the DEBUG lines above."

# Test it out
city_input = input("Enter a city: ")
result = get_outfit_suggestion(city_input)
print(result)