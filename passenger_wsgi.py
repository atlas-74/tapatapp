import os
from flask import Flask, request, render_template, redirect, url_for, jsonify
import prova


project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'app/templates')
static_path = os.path.join(project_root, 'app/static')
app = Flask(__name__, template_folder=template_path, static_folder=static_path)

@app.route('/')
def index():
    return 'Hello from flask'
    
@app.route('/get_data', methods=['GET'])
def get_data():
    # Example data
    data = {
        "status": "success",
        "message": "This is a JSON response",
        "data": {
            "id": 1,
            "name": "Sample Item"
        }
    }
    # Return JSON response
    return jsonify(data)

@app.route('/prova2', methods=['GET'])
def prova2():
	return prova.provaFunc()

application = app
app.run(debug=True)
