"""SIMULADOR DE SENSOR DE TEMPERATURA
"""
from flask import Flask, jsonify
import random, time

app = Flask(__name__)


@app.route('/get_temperature', methods=['GET'])
def get_temperature():
    temperature = round(random.uniform(4, 40), 2)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return jsonify({'temperature': temperature, 'timestamp': timestamp})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
