#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/states')
def statesList():
    n = storage.all("State")
    return render_template('9-states.html', n=n)


@app.route('/states/<id>')
def statesId(id):
    o = storage.all("State")
    identity = ""
    for i in o:
        if id == i:
            identity = o[i]
    return render_template('9-states.html', identity=identity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
