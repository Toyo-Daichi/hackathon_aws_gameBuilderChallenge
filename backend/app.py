#-*- coding: utf-8 -*-
"""
Created on 2024.01.13
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from context.db import Db
from infrastructure.db.character import CharacterQuery
from infrastructure.db.score import ScoreRepository, ScoreQuery

from util.logger import Logger
logging = Logger(__name__, "INFO")

app = Flask(__name__)
CORS(app)
db = Db()

character_query = CharacterQuery(db.pool)
score_query = ScoreQuery(db.pool)
score_repository = ScoreRepository(db.pool)

@app.route('/characters', methods=['GET'])
def get_characters():
    _characters = character_query.find_all_character()
    characters = [character.to_dict() for character in _characters]
    return jsonify(characters)

@app.route('/characters/id/<int:id>', methods=['GET'])
def get_character_by_id(id):
    character = character_query.find_character_by_id(id)
    return jsonify(character.to_dict())

@app.route('/characters/name/<string:name>', methods=['GET'])
def get_character_by_name(name):
    character = character_query.find_character_by_name(name)
    return jsonify(character.to_dict())

@app.route('/characters/role/<string:role>', methods=['GET'])
def get_character_by_role(role):
    _characters = character_query.find_character_by_role(role)
    characters = [character.to_dict() for character in _characters]
    return jsonify(characters)

@app.route('/scores', methods=['GET'])
def get_scores():
    _scores = score_query.find_all_score()
    scores = [score.to_dict() for score in _scores]
    return jsonify(scores)

@app.route('/scores/id/<int:id>', methods=['GET'])
def get_score_by_id(id):
    score = score_query.find_score_by_id(id)
    return jsonify(score.to_dict())

@app.route('/scores/mode/<string:mode>', methods=['GET'])
def get_score_by_mode(mode):
    _scores = score_query.find_score_by_mode(mode)
    scores = [score.to_dict() for score in _scores]
    return jsonify(scores)

@app.route('/scores', methods=['POST'])
def create_score():
    data = request.get_json()
    mode = data['mode']
    score = data['score']
    score = ScoreRepository(db.pool).write_score(1, mode, score)
    return jsonify(score)

if __name__ == '__main__':  
    app.run(host="0.0.0.0", port=5000, debug=False)
