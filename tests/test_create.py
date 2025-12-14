import json

# CREATE HERO TESTS

def test_create_hero_success(client, auth_headers):
    # Test post new hero
    new_hero = {
        'hero_name': 'Test Hero',
        'attack_type': 'Melee',
        'attribute_id': 1,
        'role_id': 2
    }
    
    response = client.post('/api/heroes',
                          data=json.dumps(new_hero),
                          headers=auth_headers)
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['message'] == 'Hero created successfully'
    assert 'hero_id' in data['data']
    assert data['data']['hero_name'] == 'Test Hero'
    assert data['created_by'] == 'testuser'
    
    # Delete the test hero
    hero_id = data['data']['hero_id']
    client.delete(f'/api/heroes/{hero_id}', headers=auth_headers)


def test_create_hero_missing_required_fields(client, auth_headers):
    # Test post hero with missing required fields, ex no attack type
    invalid_hero = {
        'hero_name': 'Test Hero'
        # Missing attack_type
    }
    
    response = client.post('/api/heroes',
                          data=json.dumps(invalid_hero),
                          headers=auth_headers)
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False
    assert 'error' in data


def test_create_hero_no_data(client, auth_headers):
    # Test post hero with no data
    response = client.post('/api/heroes',
                          data=json.dumps({}),
                          headers=auth_headers)
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False


def test_create_hero_name_too_long(client, auth_headers):
    # Test post hero with name > 50 characters
    invalid_hero = {
        'hero_name': 'A' * 51,  # 51 length
        'attack_type': 'Melee'
    }
    
    response = client.post('/api/heroes',
                          data=json.dumps(invalid_hero),
                          headers=auth_headers)
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False
    assert 'hero_name' in data['error']


def test_create_hero_attack_type_too_long(client, auth_headers):
    # Test post hero with attack_type > 10 characters
    invalid_hero = {
        'hero_name': 'Test Hero',
        'attack_type': 'A' * 11  # 11 characters
    }
    
    response = client.post('/api/heroes',
                          data=json.dumps(invalid_hero),
                          headers=auth_headers)
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False


def test_create_hero_without_token(client):
    # Test post hero without JWT token
    new_hero = {
        'hero_name': 'Test Hero',
        'attack_type': 'Melee'
    }
    
    response = client.post('/api/heroes',
                          data=json.dumps(new_hero),
                          content_type='application/json')
    
    assert response.status_code == 401
