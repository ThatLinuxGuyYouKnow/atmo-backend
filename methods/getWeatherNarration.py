 
def getTempDescription(temp):
    if temp < 0:
        return 'Freezing'
    if temp < 10:
        return 'Cold'
    if temp < 17:
        return 'Cool'
    if temp < 24:
        return 'Mild'
    if temp < 30:
        return 'Warm'
    return 'Hot'

def getCloudDescription(cloudCover):
    if cloudCover < 25:
        return 'Clear and sunny'
    if cloudCover < 50:
        return 'Partly cloudy'
    if cloudCover < 85:
        return 'Mostly cloudy'
    return 'Overcast'

def getWindDescription(windSpeed, windGust):
 
    if windGust > 40 or windSpeed > 25:
        return 'very windy with strong gusts'
    if windGust > 25 or windSpeed > 15:
        return 'breezy'
    return None  

 
def generateWeatherSummary(values):
    # Extracting variables
    temp = values['temperatureAvg']
    cloudCover = values['cloudCoverAvg']
    windSpeed = values['windSpeedAvg']
    windGust = values['windGustMax']
    snowIntensity = values['snowIntensityAvg']
    rainIntensity = values['rainIntensityAvg']
    
    summary_parts = []

 
    if snowIntensity > 1.0:
        summary_parts.append("Heavy snow")
    elif snowIntensity > 0.1:
        summary_parts.append("Light snow")
    elif rainIntensity > 1.0:
        summary_parts.append("Rainy")
    elif rainIntensity > 0.1:
        summary_parts.append("Light showers")

    # PRIORITY 2: SKY (if no precipitation was found)
    # 'if not summary_parts' is the Pythonic way to check if a list is empty
    if not summary_parts:
        summary_parts.append(getCloudDescription(cloudCover))

    # PRIORITY 3: TEMPERATURE (Almost always add this)
    # Note the use of .lower()
    summary_parts.append("and " + getTempDescription(temp).lower())
    
    # PRIORITY 4: WIND (Add if notable)
    wind_desc = getWindDescription(windSpeed, windGust)
    if wind_desc: # This works because None evaluates to False
        summary_parts.append("with " + wind_desc + " conditions")

 
    return ' '.join(summary_parts)

 
 
 
 
 