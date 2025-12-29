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

with st.sidebar:
    st.header("Settings")
    unit_choice = st.radio("Choose Units:", ["Fahrenheit (°F)", "Celsius (°C)"])

unit_system = "imperial" if unit_choice == "Fahrenheit (°F)" else "metric"
temp_symbol = "°F" if unit_system == "imperial" else "°C"

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

        threshold_cold = 50 if unit_system == "imperial" else 10
        threshold_warm = 70 if unit_system == "imperial" else 21

        if temp < threshold_cold:
            st.info("🧥 **Outfit Suggestion:** It's cold! Wear a heavy coat and scarf.")
        elif temp < threshold_warm:
            st.warning("🍂 **Outfit Suggestion:** Chilly. A light jacket or hoodie is best.")
        else:
            st.success("☀️ **Outfit Suggestion:** T-shirt and shorts weather!")
            
    else:
        st.error(f"Could not find city: {city}. Check your spelling!")