
import json

def test_delete_hero_success(client, auth_headers):
    # First create a test hero to delete
    new_hero = {
        'hero_name': 'Delete Test Hero',
        'attack_type': 'Melee',
        'attribute_id': 1,
        'role_id': 2
    }
    create_response = client.post('/api/heroes',
                                 data=json.dumps(new_hero),
                                 headers=auth_headers)
    hero_id = json.loads(create_response.data)['data']['hero_id']
    
    # Delete the hero
    response = client.delete(f'/api/heroes/{hero_id}', headers=auth_headers)
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['message'] == 'Hero deleted successfully'
    assert data['deleted_by'] == 'testuser'
    
    # Verify 
    get_response = client.get(f'/api/heroes/{hero_id}', headers=auth_headers)
    assert get_response.status_code == 404


def test_delete_hero_not_found(client, auth_headers):
    # Test deleting non-existent hero
    response = client.delete('/api/heroes/999', headers=auth_headers)
    
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['success'] == False
    assert 'error' in data


def test_delete_hero_without_token(client):
    # Test deleting hero without JWT token (should fail)
    response = client.delete('/api/heroes/1')
    assert response.status_code == 401
