import streamlit as st
import requests
from datetime import date

api_key = "x1I5fdzd7jqpICqhquppDNNzsgekH4dI3DDRYcsp"

now = date.today()
# print(now)

st.set_page_config(layout="wide")

now = st.text_input(label="Enter the date in the format YYYY-MM-DD :", value=now, key="new_date")

url = "https://api.nasa.gov/planetary/apod?" \
       f"date={now}&" \
       f"api_key={api_key}"


# Get image of the day from the NASA library
response = requests.get(url)
content = response.json()

# Get the name of the image url
hold = content["url"]
explanation = content["explanation"]
title = content["title"]

# Get the binary data of the picture
picture = requests.get(hold)

# Open a file to save the image in
with open("image.jpg", "wb") as file:
       file.write(picture.content)

# Start the web app
st.title(title)
col1, col2 = st.columns(2)
with col1:
       st.image("image.jpg")

with col2:
       st.info(explanation)
       st.info(now)

       # now = input("Enter the date in the format YYYY-MM-DD :")
# print(now)