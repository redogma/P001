import os
import json

from flask import Flask, jsonify, abort, make_response, render_template, redirect

app = Flask(__name__)
APP_NAME = os.environ['APP_NAME']

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': '404 - Not found'}), 404)

@app.errorhandler(500)
def error_500(error):
	return make_response(jsonify({'error': '500 - Internal application error'}), 500)

@app.route('/')
def index():
	return redirect('/home/')

@app.route('/healthcheck')
def root():
    return 'Healthcheck %s' % (APP_NAME,)

@app.route('/home/')
@app.route('/home/<name>')
def home(name=None):
	return render_template('home.html', name=name)

@app.route('/elevations/')
def elevations(name=None):
	data=[{'pos': 1 ,'elevation': 52, 'run': 'Test'}]
	filter=None
	return render_template('elevations.html', filter=filter, data=data,count=len(data))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
