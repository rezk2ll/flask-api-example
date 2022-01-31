from flask import Blueprint, jsonify
import re

clean_blueprint = Blueprint('clean_module', __name__)

def clean(text):
  return re.sub(r'(^|\s)euh($|\s)', '', text)

@clean_blueprint.route('/clean/<text>', methods=['GET'])
def clean_text_from_get(text):
  if text is None:
    return jsonify({'error': 'No text provided'}), 400
  else:
    return jsonify({'text': clean(text)}), 200

@clean_blueprint.route('/clean', methods=['POST'])
def clean_text_from_post():
  text = request.get_json()['text']
  if text is None:
    return jsonify({'error': 'No text provided'}), 400
  else:
    return jsonify({'text': clean(text)}), 200
