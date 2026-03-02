import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

try:
    API_KEY = st.secrets["OPENWEATHER_API_KEY"]
except (KeyError, FileNotFoundError, Exception):
    API_KEY = os.getenv("OPENWEATHER_API_KEY")

st.set_page_config(page_title="Weather Outfit Pro", page_icon="🌤️")

# -------- Outfit Recommendation Engine --------
def get_outfit_suggestion(temp, condition, unit_system):
    condition = condition.lower()

    if unit_system == "imperial":
        if temp < 32:
            return "🧊 Heavy winter coat, gloves, scarf, and boots"
        elif temp < 45:
            return "🧥 Wool coat, sweater, and jeans"
        elif temp < 55:
            return "🧣 Light jacket or hoodie with long sleeves"
        elif temp < 60:
            return "👕 Long sleeve shirt and pants"
        elif temp < 70:
            return "👕 T-shirt with jeans or light pants"
        elif temp < 80:
            return "👕 T-shirt and shorts"
        elif temp < 90:
            return "🩳 Tank top, shorts, sunglasses"
        else:
            return "☀️ Ultra hot! Tank top, athletic shorts, and sunscreen"

    else:  # Celsius
        if temp < 0:
            return "🧊 Heavy winter coat, gloves, scarf, and boots"
        elif temp < 7:
            return "🧥 Wool coat, sweater, and jeans"
        elif temp < 13:
            return "🧣 Light jacket or hoodie with long sleeves"
        elif temp < 16:
            return "👕 Long sleeve shirt and pants"
        elif temp < 21:
            return "👕 T-shirt with jeans or light pants"
        elif temp < 27:
            return "👕 T-shirt and shorts"
        elif temp < 32:
            return "🩳 Tank top, shorts, sunglasses"
        else:
            return "☀️ Ultra hot! Tank top, athletic shorts, and sunscreen"


def weather_modifier(condition):
    condition = condition.lower()

    if "rain" in condition:
        return "☔ Bring an umbrella or rain jacket."
    elif "snow" in condition:
        return "❄️ Wear waterproof boots and warm layers."
    elif "thunderstorm" in condition:
        return "⛈️ Stay dry with a waterproof jacket."
    elif "clear" in condition:
        return "🕶️ Sunglasses recommended."
    elif "cloud" in condition:
        return "🌥️ Light layers recommended."
    elif "mist" in condition or "fog" in condition:
        return "🌫️ Consider a light jacket due to damp conditions."
    else:
        return ""


# -------- Sidebar --------
with st.sidebar:
    st.header("Settings")
    unit_choice = st.radio("Choose Units:", ["Fahrenheit (°F)", "Celsius (°C)"])

unit_system = "imperial" if unit_choice == "Fahrenheit (°F)" else "metric"
temp_symbol = "°F" if unit_system == "imperial" else "°C"


# -------- Main App --------
st.title("🌤️ Weather Outfit Planner")

city = st.text_input("City Name", placeholder="e.g. Shanghai")

if city:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={unit_system}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temp = data['main']['temp']
        condition = data['weather'][0]['main']

        col1, col2 = st.columns(2)

        col1.metric("Temperature", f"{temp}{temp_symbol}")
        col2.metric("Condition", condition)

        outfit = get_outfit_suggestion(temp, condition, unit_system)
        modifier = weather_modifier(condition)

        st.subheader("👕 Outfit Recommendation")
        st.success(outfit)

        if modifier:
            st.info(modifier)

    else:
        st.error(f"Could not find city: {city}. Check your spelling!")