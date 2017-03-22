from flask import render_template, request, url_for, jsonify
from webapp import app, model

@app.route('/', methods=['POST', 'GET'])
def index():
    return "Hello world!"

@app.route('/providers', methods=['GET'])
def providers():
    return jsonify({"providers": model.get_all_providers()})

@app.route('/programs/<int:provider_id>', methods=['GET'])
def programs(provider_id):
    return jsonify({"programs": model.get_programs_for_provider(provider_id)})

@app.route('/outcomes/<int:provider_id>/<int:program_id>', methods=['GET'])
def outcomes(provider_id, program_id):
    return jsonify({"outcomes": model.get_outcomes_for_program(provider_id, program_id)})
