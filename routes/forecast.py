import os
import requests
from methods.getWeatherNarration import generateWeatherSummary

apikey = os.environ['TOMORROW_KEY']

def return_forecast(longlat: str):
    """Fetches today's hourly forecast and returns 4 equidistant summaries."""

    url = f"https://api.tomorrow.io/v4/weather/forecast?location={longlat}&apikey={apikey}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Step 1: Slice first 24 hourly entries (i.e., today's data)
    full_hourly = data.get("timelines", {}).get("hourly", [])
    today_hourly = full_hourly[:24]

    if len(today_hourly) < 4:
        raise ValueError("Less than 4 hourly data points available for today.")

    # Step 2: Select 4 equidistant indices
    step = len(today_hourly) // 4
    selected_indices = [step * i for i in range(4)]

    # Step 3: Generate weather summaries
    narration_list = []
    for idx in selected_indices:
        hour_data = today_hourly[idx]
        summary = f"{hour_data['time']}: {generateWeatherSummary(hour_data['values'])}"
        narration_list.append(summary)

    return narration_list
