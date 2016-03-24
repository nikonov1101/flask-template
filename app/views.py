"""
    Simple View module example
"""

from flask import request, render_template
from app import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """ Render index page, if POST-ing data - payload also will be rendered """

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        request_payload = request.data
        return render_template('index.html', request_payload=request_payload)
