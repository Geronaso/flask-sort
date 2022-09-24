"""This file contains the Endpoints of our API"""

from flask import (
    Blueprint, request, jsonify, abort
)

from flask_sort.models import vowel_count, sort

bp = Blueprint('views', __name__)

@bp.route('/vowel_count', methods=['POST'])
def route_vowel_count():
    """Vowel count Endpoint"""
    request_data = request.get_json()
    # Some basic check to check the data received.
    if not 'words' in request_data or not request_data['words'] \
    or not isinstance(request_data['words'], list) \
    or not all(isinstance(item, str) for item in request_data['words']):
        abort(400)
    # If the format is correct pass the value to function to count the vowels
    response = vowel_count(request_data['words'])
    return jsonify(response)


@bp.route('/sort', methods=['POST'])
def route_sort():
    """Sort Endpoint"""
    request_data = request.get_json()
    # Some basic check to check the data received
    order = ['asc', 'desc']
    if not 'words' in request_data or not request_data['words'] \
    or not isinstance(request_data['words'], list) \
    or not all(isinstance(item, str) for item in request_data['words']):
        abort(400)
    elif not 'order' in request_data or request_data['order'] not in order \
    or not isinstance(request_data['order'], str):
        abort(400)
    response = sort(request_data['words'], request_data['order'])
    return jsonify(response)
