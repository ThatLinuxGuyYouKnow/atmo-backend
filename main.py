
from flask import Flask,request
from flask import jsonify
from routes.forecast import return_forecast

app = Flask(__name__)

@app.route('/forecast',methods=['GET', 'POST'])
def get_forecast():
    if request.method == 'POST':
     data = request.get_json()
     location = data.get("location")
     response = return_forecast(longlat=location)
     print(response)
     return jsonify({'message': 'response'})


app.run(debug=True, host='0.0.0.0', port=5000)
