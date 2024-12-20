from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_sensor_data():
    temperature = round(random.uniform(5, 35), 2)
    humidity = round(random.uniform(20, 90), 2)
    return jsonify({'temperature': temperature, 'humidity': humidity})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
