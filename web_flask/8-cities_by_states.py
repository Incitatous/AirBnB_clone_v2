#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/cities_by_states')
def statesList():
    n = storage.all("State")
    return render_template('8-cities_by_states.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
