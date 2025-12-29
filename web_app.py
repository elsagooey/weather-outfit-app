import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Page Config
st.set_page_config(page_title="Weather Outfit Pro", page_icon="🌤️")

st.title("🌤️ Weather Outfit Planner")
st.write("Enter your city to get the perfect outfit recommendation.")

city = st.text_input("City Name", placeholder="e.g. Shanghai")

if city:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        condition = data['weather'][0]['main']
        
        # UI Columns
        col1, col2 = st.columns(2)
        col1.metric("Temperature", f"{temp}°F")
        col2.metric("Condition", condition)

        # Logic
        if temp < 50:
            st.info("🧥 **Outfit Suggestion:** It's cold! Wear a heavy coat and scarf.")
        elif temp < 70:
            st.warning("🍂 **Outfit Suggestion:** Chilly. A light jacket or hoodie is best.")
        else:
            st.success("☀️ **Outfit Suggestion:** T-shirt and shorts weather!")
            
    else:
        st.error(f"Could not find city: {city}. Check your spelling!")