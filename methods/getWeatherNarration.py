def getTempDescription(temp):
    if (temp < 0):
         return 'Freezing'
    if (temp < 10):
         return 'Cold'
    if (temp < 17):
         return 'Cool'
    if (temp < 24):
         return 'Mild'
    if (temp < 30):
         return 'Warm'
    return 'Hot'


def getCloudDescription(cloudCover) :
    if (cloudCover < 25):
         return 'Clear and sunny'
    if (cloudCover < 50):
         return 'Partly cloudy'
    if (cloudCover < 85):
         return 'Mostly cloudy'
    return 'Overcast'


def getWindDescription(windSpeed, windGust) :
    if (windGust > 40 or windSpeed > 25):
         return 'Very windy with strong gusts'
    if (windGust > 25 or windSpeed > 15):
         return 'Breezy'
    return null


def getHumidityDescription(humidity, temp) :
    if (temp > 24 and humidity > 70):
         return 'and humid'
    if (temp > 24 and humidity < 35):
         return 'and dry'
    return ''
