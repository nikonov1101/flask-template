__author__ = 'sshaman'

from flask import request, render_template, flash, redirect, jsonify
from app import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        request_payload = request.data
        return render_template('index.html', request_payload=request_payload)