
from flask import Flask,request
from flask import jsonify
from routes.forecast import return_forecast

app = Flask(__name__)

@app.route('/forecast',methods=['GET', 'POST'])
def get_forecast(location_name):
    if request.method == 'POST':

     response = return_forecast(longlat=location_name)
     print(response)
     return jsonify({'message': 'response'})


app.run(debug=True, host='0.0.0.0', port=5000)
