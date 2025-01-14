import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_characters(client):
    response = client.get('/characters')
    assert response.status_code == 200

def test_get_character_by_id(client):
    response = client.get('/characters/id/1')
    assert response.status_code == 200

def test_get_character_by_name(client):
    response = client.get('/characters/name/Mario')
    assert response.status_code == 200

def test_get_character_by_role(client):
    response = client.get('/characters/role/Enemy')
    assert response.status_code == 200

def test_get_scores(client):
    response = client.get('/scores')
    assert response.status_code == 200

def test_get_score_by_id(client):
    response = client.get('/scores/id/1')
    assert response.status_code == 200

def test_get_score_by_score(client):
    response = client.get('/scores/mode/DoS')
    assert response.status_code == 200

def test_create_score(client):
    response = client.post('/scores', json={"mode":"DoS", "score":100})
    assert response.status_code == 200
