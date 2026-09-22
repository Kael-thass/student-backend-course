#imports
from flask import Flask, jsonify, request
import time

app = Flask(__name__)

cities = [
    {
        'id': 1,
        'name': 'Moscow',
        'ppl': 123456789,
        'country': 'Russia',
        'size': 1234
    },
    {
        'id': 2,
        'name': 'St. Petersburg',
        'ppl': 1234567,
        'country': 'Russia',
        'size': 321
    },
]
@app.before_request
def log_request():
    print(f'[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}] {request.method} {request.path}')

#base lvl
@app.route('/cities')
def get_cities():
    return jsonify({
        'count': len(cities),
        'cities': cities
    })

@app.route('/cities/<int:city_id>')
def get_city(city_id):
    city = next((c for c in cities if c['id'] == city_id), None)
    if not city:
        return jsonify({
            'error': 'city not found',
        }), 404
    return jsonify(city)

@app.route('/cities/<int:city_id>/size')
def get_city_size(city_id):
    city = next((c for c in cities if c[
        'id'] == city_id), None)
    if not city:
        return jsonify({
            'error': 'city not found'
        }), 404
    return jsonify({
        'city': city['name'],
        'size': city['size'],
        'unit': 'kmsq'
    })

@app.route('/countries/<string:country>/cities')
def get_country_cities(country):
    filtered = [c for c in cities if c[
        'country'
    ].lower() == country.lower()
                ]
    return jsonify({
        'country': country,
        'count': len(filtered),
        cities: filtered
    })

if __name__ == '__main__':
    app.run(port = 3000, debug=True)