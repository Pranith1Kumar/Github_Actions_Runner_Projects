import os
import requests
import smtplib
from email.message import EmailMessage

# Read values from environment variables
API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(url).json()
    weather = response['weather'][0]['description']
    return weather

def send_email(weather):
    msg = EmailMessage()
    msg['Subject'] = f"Weather Update for {CITY}"
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    msg.set_content(f"The current weather in {CITY} is: {weather}.")

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    weather = get_weather()
    send_email(weather)
