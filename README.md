# CSE-Flask

A Flask REST API for managing Dota 2 heroes. Has JWT authentication, CRUD operations, and search.


## What was done

- JWT Authentication
- CRUD Operations (Create, Read, Update, Delete)
- Search heroes by name, attack type, attribute, or role
- JSON and XML response formats
- Input validation
- 34 automated tests

## Installation

1. Clone the repository
```
git clone https://github.com/Ritvent/CSE-Flask.git
cd CSE-Flask
```

2. Create virtual environment
```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up database - Create a MySQL database named `finaldbcselec` and import:
```
mysql -u root -p finaldbcselec < database/dump.sql
```

5. Create `.env` file in root folder:
```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=finaldbcselec
JWT_SECRET_KEY=your-secret-key
```


## How to Run

```
python app.py
```

Server runs at http://127.0.0.1:5000


## API Endpoints

Public (No Token):
- GET / - Home
- POST /api/login - Get token

Protected (Need Token):
- GET /api/heroes - Get all heroes
- GET /api/heroes/<id> - Get one hero
- POST /api/heroes - Create hero
- PUT /api/heroes/<id> - Update hero
- DELETE /api/heroes/<id> - Delete hero


## How to Use

1. Login first to get token:

POST /api/login
```
{
  "testusername": "user",
  "testpassword": "pass"
}
```

2. Use the token in Authorization header:
```
Authorization: Bearer <your_token>
```


## Search Parameters

You can filter heroes using these URL parameters:
- hero_name - Filter by name
- attack_type - Filter by Melee or Ranged
- attribute_id - Filter by attribute
- role_id - Filter by role
- format - json or xml

Example: /api/heroes?hero_name=Axe&attack_type=Melee


## Create Hero

POST /api/heroes
```
{
  "hero_name": "New Hero",
  "attack_type": "Melee",
  "attribute_id": 1,
  "role_id": 1
}
```

Required fields: hero_name, attack_type


## Update Hero

PUT /api/heroes/1
```
{
  "hero_name": "Updated Name"
}
```


## Delete Hero

DELETE /api/heroes/1

## Test edge cases

Run all tests:
```
pytest -v
```
