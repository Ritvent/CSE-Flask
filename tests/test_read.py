import json


# GET ALL HEROES TESTS


def test_get_all_heroes_success(client, auth_headers):
    # Test get all heroes with valid token
    response = client.get('/api/heroes', headers=auth_headers)
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert 'data' in data
    assert 'count' in data
    assert isinstance(data['data'], list)
    assert data['authenticated_user'] == 'testuser'


def test_get_heroes_json_format(client, auth_headers):
    # Test get heroes JSON by default
    response = client.get('/api/heroes', headers=auth_headers)
    assert response.content_type == 'application/json'


def test_get_heroes_xml_format(client, auth_headers):
    # Test get heroes returns XML when opted
    response = client.get('/api/heroes?format=xml', headers=auth_headers)
    assert response.status_code == 200
    assert response.content_type == 'application/xml'



def test_search_heroes_by_name(client, auth_headers):
    # Test get heroes by name
    response = client.get('/api/heroes?hero_name=mage', headers=auth_headers)
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['search_filters']['hero_name'] == 'mage'


def test_search_heroes_by_attack_type(client, auth_headers):
    # Test get heroes by attack type
    response = client.get('/api/heroes?attack_type=Melee', headers=auth_headers)
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['search_filters']['attack_type'] == 'Melee'


def test_search_heroes_by_attribute(client, auth_headers):
    """Test searching heroes by attribute_id"""
    response = client.get('/api/heroes?attribute_id=1', headers=auth_headers)
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['search_filters']['attribute_id'] == '1'


def test_search_heroes_by_role(client, auth_headers):
    # Test get heroes by role_id
    response = client.get('/api/heroes?role_id=2', headers=auth_headers)
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['search_filters']['role_id'] == '2'


def test_search_heroes_multiple_filters(client, auth_headers):
    # Test get heroes with multiple filters
    response = client.get('/api/heroes?attack_type=Ranged&attribute_id=2', 
                         headers=auth_headers)
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True


def test_get_single_hero_success(client, auth_headers):
    # Test get one hero by ID
    response = client.get('/api/heroes/1', headers=auth_headers)
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert 'data' in data
    assert data['data']['hero_id'] == 1


def test_get_single_hero_not_found(client, auth_headers):
    # Test get non-existent hero record
    response = client.get('/api/heroes/999', headers=auth_headers)
    
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['success'] == False
    assert 'error' in data


def test_get_single_hero_without_token(client):
    # Test get single hero without token
    response = client.get('/api/heroes/1')
    assert response.status_code == 401
