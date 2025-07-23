from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/forecast')
def get_forecast():
    return jsonify({'message': 'Forecast endpoint'})


app.run(debug=True, host='0.0.0.0', port=5000)
