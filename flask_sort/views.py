from flask import (
    Blueprint, request, jsonify, abort
)

from flask_sort.models import vowel_count, sort

bp = Blueprint('views', __name__)

@bp.route('/vowel_count', methods=['POST'])
def route_vowel_count():
    request_data = request.get_json()
    # Some basic check to check the data received. Checks if it is a list, the list is not empty and the key value is words
    if not 'words' in request_data or not request_data['words'] or type(request_data['words']) is not list:
        abort(400)
    # If the format is correct pass the value to function to count the vowels
    response = vowel_count(request_data['words'])
    return jsonify(response)


@bp.route('/sort', methods=['POST'])
def route_sort():
    request_data = request.get_json()
    # The same check as the other function, instead it also checks for the key order and
    # The order array is used to check the two specific values of order
    order = ['asc', 'desc']
    if not 'words' in request_data or not request_data['words'] or type(request_data['words']) is not list:
        abort(400)
    elif not 'order' in request_data or request_data['order'] not in order or type(request_data['order']) is not str:
        abort(400)
    response = sort(request_data['words'], request_data['order'])
    return jsonify(response)