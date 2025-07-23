from flask import Flask
from flask import jsonify
from routes.forecast import return_forecast

app = Flask(__name__)

@app.route('/forecast')
def get_forecast():
    response = return_forecast()
    print(response)
    return jsonify({'message': 'response'})


app.run(debug=True, host='0.0.0.0', port=5000)
