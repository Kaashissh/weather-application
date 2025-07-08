import requests
import streamlit as st
import json

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://tse1.mm.bing.net/th/id/OIP.OCUAG2u1FSvvUJduRPEgkQHaE8?pid=Api&P=0&h=220");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;

        body, .stApp {
        color: white;  /* Sets default text color */
    }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Weather Application")
with open('data1.json') as file:
    data=json.load(file)

states=data.keys()

city_name = ""

st.subheader("select the state")
state_name=st.selectbox(label="select the state",options=states)

if state_name:
    cities=data[state_name]
    st.subheader("select the city")
    city_name = st.selectbox(label="select the city",options=cities)

if city_name:
    api_key = "3bc8c13b237018dc375fadb68d50674a"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_name}&APPID={api_key}&units=metric"

    response=requests.get(url)
    if response.status_code == 200:
       data= response.json()
       st.write(f"current whether condition: {data['weather'][0]['main']}")
       st.write(f"current temperature: {data['main']['temp']}°C.")
       st.write(f"temperature feels like: {data['main']['feels_like']}°C.")
       st.write(f"Humidity: {data['main']['humidity']}%.")
    else:
       print("Error occured , please check the city name or state name is corect or not!")