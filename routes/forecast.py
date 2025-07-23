import requests
import os

apikey = os.environ['TOMORROW_KEY']
async def returnForecast(longlat: str) :
    response = await requests.get(f'https://api.tomorrow.io/v4/weather/forecast?location=${longlat}&apikey=${apikey}')
    values = response['timelines']['minutely']