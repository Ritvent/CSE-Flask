import json

def test_home_endpoint(client):
    # Test the home endpoint
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert 'database' in data


def test_full_crud_cycle(client, auth_headers):
    # Test complete crud
    
    # CREATE
    new_hero = {
        'hero_name': 'Integration Test Hero',
        'attack_type': 'Melee',
        'attribute_id': 1,
        'role_id': 2
    }
    create_response = client.post('/api/heroes',
                                 data=json.dumps(new_hero),
                                 headers=auth_headers)
    assert create_response.status_code == 201
    hero_id = json.loads(create_response.data)['data']['hero_id']
    
    # READ/GET
    read_response = client.get(f'/api/heroes/{hero_id}', headers=auth_headers)
    assert read_response.status_code == 200
    read_data = json.loads(read_response.data)
    assert read_data['data']['hero_name'] == 'Integration Test Hero'
    
    # UPDATE
    update_data = {'attack_type': 'Ranged'}
    update_response = client.put(f'/api/heroes/{hero_id}',
                                data=json.dumps(update_data),
                                headers=auth_headers)
    assert update_response.status_code == 200
    
    # Verify update
    verify_response = client.get(f'/api/heroes/{hero_id}', headers=auth_headers)
    verify_data = json.loads(verify_response.data)
    assert verify_data['data']['attack_type'] == 'Ranged'
    
    # DELETE
    delete_response = client.delete(f'/api/heroes/{hero_id}', headers=auth_headers)
    assert delete_response.status_code == 200
    
    # Verify deletion
    final_response = client.get(f'/api/heroes/{hero_id}', headers=auth_headers)
    assert final_response.status_code == 404
