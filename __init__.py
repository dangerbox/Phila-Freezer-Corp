#-*- coding: utf-8 -*-
import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO

async_mode = 'eventlet'
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index')
def index_alt():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/temperature')
def temperature():
	return render_template('temperature.html')

@app.route('/boiler')
def boiler():
	return render_template('boiler.html')

@app.route('/thirdcontroller')
def thirdcontroller():
	return render_template('thirdcontroller.html')




if __name__ == '__main__':
	socketio.run(app)
