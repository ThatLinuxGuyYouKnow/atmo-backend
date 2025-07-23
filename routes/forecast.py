import os
import requests
from methods.getWeatherNarration import generateWeatherSummary

apikey = os.environ['TOMORROW_KEY']

def return_forecast(longlat: str):
    """Fetches minute-by-minute forecast and returns a list of narration strings."""
 
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={longlat}&apikey={apikey}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

 
    values = data.get("timelines", {}).get("minutely", [])
    narration_list = []

  
    for minute_data in values:
        summary = generateWeatherSummary(minute_data)
        narration_list.append(summary)

    return narration_list
