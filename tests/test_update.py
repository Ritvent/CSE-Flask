import json


def test_update_hero_success(client, auth_headers):
    # First create a hero for PUT testing
    new_hero = {
        'hero_name': 'Update Test Hero',
        'attack_type': 'Melee',
        'attribute_id': 1,
        'role_id': 2
    }
    create_response = client.post('/api/heroes',
                                 data=json.dumps(new_hero),
                                 headers=auth_headers)
    hero_id = json.loads(create_response.data)['data']['hero_id']
    
    # Update the hero
    update_data = {
        'attack_type': 'Ranged'
    }
    response = client.put(f'/api/heroes/{hero_id}',
                         data=json.dumps(update_data),
                         headers=auth_headers)
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['message'] == 'Hero updated successfully'
    assert data['updated_by'] == 'testuser'
    
    # Clean up
    client.delete(f'/api/heroes/{hero_id}', headers=auth_headers)


def test_update_hero_not_found(client, auth_headers):
    # Test updating non-existent hero
    update_data = {
        'attack_type': 'Ranged'
    }
    response = client.put('/api/heroes/99999',
                         data=json.dumps(update_data),
                         headers=auth_headers)
    
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['success'] == False


def test_update_hero_no_data(client, auth_headers):
    # Test updating hero with no data
    response = client.put('/api/heroes/1',
                         data=json.dumps({}),
                         headers=auth_headers)
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False


def test_update_hero_no_fields_to_update(client, auth_headers):
    # Create a test hero first for testing without fields
    new_hero = {
        'hero_name': 'Test Hero',
        'attack_type': 'Melee',
        'attribute_id': 1,
        'role_id': 1
    }
    create_response = client.post('/api/heroes',
                                 data=json.dumps(new_hero),
                                 headers=auth_headers)
    hero_id = json.loads(create_response.data)['data']['hero_id']
    
    # Try to update with empty valid fields
    response = client.put(f'/api/heroes/{hero_id}',
                         data=json.dumps({'invalid_field': 'value'}),
                         headers=auth_headers)
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False
    
    # Clean up
    client.delete(f'/api/heroes/{hero_id}', headers=auth_headers)


def test_update_hero_name_too_long(client, auth_headers):
    # Test update hero name with > 50 characters
    update_data = {
        'hero_name': 'A' * 51
    }
    response = client.put('/api/heroes/1',
                         data=json.dumps(update_data),
                         headers=auth_headers)
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False


def test_update_hero_without_token(client):
    # Test updating hero without JWT token
    update_data = {
        'attack_type': 'Ranged'
    }
    response = client.put('/api/heroes/1',
                         data=json.dumps(update_data),
                         content_type='application/json')
    
    assert response.status_code == 401
