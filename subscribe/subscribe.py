from flask import Flask, request, Response, abort, render_template, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from collections import defaultdict

import paho.mqtt.client as mqtt
import mysql.connector

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)