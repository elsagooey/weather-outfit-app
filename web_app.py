import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = st.secrets.get("OPENWEATHER_API_KEY") or os.getenv("OPENWEATHER_API_KEY")


st.set_page_config(page_title="Weather Outfit Pro", page_icon="🌤️", layout="centered")


st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #e0f2fe, #ffffff);
    }
    div[data-testid="stMetricValue"] {
        font-size: 40px;
        color: #0369a1;
    }
    .stButton>button {
        border-radius: 20px;
        background-color: #0ea5e9;
        color: white;
    }
    </style>
    """, unsafe_allow_code=True)

# 3. App Header
st.title("🌤️ Weather Outfit Planner")
st.markdown("---") # Visual divider

# 4. Input Area (Using a container to group it)
with st.container():
    city = st.text_input("📍 Where are you headed?", placeholder="e.g. Shanghai")

if city:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        condition = data['weather'][0]['main']
        humidity = data['main']['humidity']

        with st.container(border=True):
            st.subheader(f"Current Weather in {city}")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Temp", f"{temp}°F")
            col2.metric("Status", condition)
            col3.metric("Humidity", f"{humidity}%")

            st.divider()


            if temp < 50:
                st.info("🧥 **Outfit Suggestion:** It's cold! Wear a heavy coat and scarf.")
            elif temp < 70:
                st.warning("🍂 **Outfit Suggestion:** Chilly. A light jacket or hoodie is best.")
            else:
                st.success("☀️ **Outfit Suggestion:** T-shirt and shorts weather!")
                
            if "Rain" in condition:
                st.error("☔ **Bonus Tip:** It's raining! Grab an umbrella.")
            
    else:
        st.error(f"Could not find city: {city}. Check your spelling!")