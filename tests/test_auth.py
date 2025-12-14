import json

# AUTHENTICATION TESTS

def test_login_success(client):
    # Test successful login
    response = client.post('/api/login',
                          data=json.dumps({
                              'testusername': 'testuser',
                              'testpassword': 'testpass'
                          }),
                          content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert 'access_token' in data
    assert data['username'] == 'testuser'


def test_login_missing_data(client):
    # Test login with missing data
    response = client.post('/api/login',
                          data=json.dumps({}),
                          content_type='application/json')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False
    assert 'error' in data


def test_login_missing_username(client):
    # Test without username
    response = client.post('/api/login',
                          data=json.dumps({
                              'testpassword': 'testpass'
                          }),
                          content_type='application/json')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False


def test_login_missing_password(client):
    # Test without password
    response = client.post('/api/login',
                          data=json.dumps({
                              'testusername': 'testuser'
                          }),
                          content_type='application/json')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False



# AUTHORIZATION TESTS


def test_get_heroes_without_token(client):
    # Test get heroes without JWT token
    response = client.get('/api/heroes')
    assert response.status_code == 401


def test_get_heroes_with_invalid_token(client):
    # Test get heroes with invalid JWT token
    headers = {'Authorization': 'Bearer invalid_token_here'}
    response = client.get('/api/heroes', headers=headers)
    assert response.status_code == 422  # Unprocessable Entity
