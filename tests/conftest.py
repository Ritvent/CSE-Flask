import pytest
import json
import sys
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, mysql


@pytest.fixture
def client():

    app.config['TESTING'] = True
    app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture
def auth_token(client):
    # Get JWT token 
    response = client.post('/api/login',
                          data=json.dumps({
                              'testusername': 'testuser',
                              'testpassword': 'testpass'
                          }),
                          content_type='application/json')
    data = json.loads(response.data)
    return data['access_token']


@pytest.fixture
def auth_headers(auth_token):
    # Create authorization headers with JWT token
    return {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
