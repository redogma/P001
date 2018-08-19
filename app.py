import os

from flask import Flask, jsonify, abort, make_response, render_template, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/test')
def root():
    return 'P001!'

@app.route('/home/')
@app.route('/home/<name>')
def home(name=None):
	return render_template('home.html', name=name)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
