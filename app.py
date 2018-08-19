import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/test')
def hello():
    return 'P001!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)