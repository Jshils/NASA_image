import streamlit as st
import requests
from datetime import date

now = date.today()
print(now)


api_key = "x1I5fdzd7jqpICqhquppDNNzsgekH4dI3DDRYcsp"

url = "https://api.nasa.gov/planetary/apod?" \
       f"date={now}&" \
       "api_key=x1I5fdzd7jqpICqhquppDNNzsgekH4dI3DDRYcsp"


# Get image of the day from the NASA library
response = requests.get(url)
content = response.json()

# Get the name of the image url
hold = content["url"]
explanation = content["explanation"]

# Get the binary data of the picture
picture = requests.get(hold)

# Open a file to save the image in
with open("image.jpg", "wb") as file:
       file.write(picture.content)

# Start the web app

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
       st.image("image.jpg")

with col2:
       st.info(explanation)
       st.text_input("Enter the date in the format YYYY-MM-DD :")