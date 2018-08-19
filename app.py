import os

from flask import Flask, jsonify, abort, make_response, render_template, redirect

app = Flask(__name__)

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
    return 'Healthcheck'

@app.route('/home/')
@app.route('/home/<name>')
def home(name=None):
	return render_template('home.html', name=name)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
