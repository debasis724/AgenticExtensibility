import requests
import matplotlib.pyplot as plt
import urllib3

# Disable SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current_weather=true"

response = requests.get(url, verify=False)  # <-- Add verify=False
data = response.json()

current = data["current_weather"]

labels = ["Temperature (°C)", "Wind Speed (km/h)", "Wind Direction (°)"]
values = [
    current["temperature"],
    current["windspeed"],
    current["winddirection"]
]

plt.figure()
plt.bar(labels, values)
plt.title("Mumbai Current Weather")
plt.show()
