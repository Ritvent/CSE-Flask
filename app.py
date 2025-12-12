from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


mysql = MySQL(app)

@app.route('/') # home
def index():
    return jsonify({
        'message': 'Testing!',
        'database': 'finaldbcselec'
    })

# 200 OK, 201 CREATED
# 404 NOT FOUND, 400 BAD REQUEST
# 500 Internal Server Error


# GET heroes endpoint
@app.route('/api/heroes', methods=['GET'])
def get_heroes():
    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT h.*, a.attribute_type, r.role_name 
            FROM hero h
            LEFT JOIN attribute a ON h.ATTRIBUTE_attribute_id = a.attribute_id
            LEFT JOIN role r ON h.ROLE_role_id = r.role_id
        """)
        # heroes = fetched result
        heroes = cur.fetchall()
        cur.close()
        
        # format data
        heroes_list = []
        for hero in heroes:
            heroes_list.append({
                'hero_id': hero[0],
                'hero_name': hero[1],
                'attack_type': hero[2],
                'attribute_id': hero[3],
                'role_id': hero[4],
                'attribute_type': hero[5] if len(hero) > 5 else None,
                'role_name': hero[6] if len(hero) > 6 else None
            })
        
        return jsonify({
            'success': True,
            'count': len(heroes_list),
            'data': heroes_list
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e) # display error message
        }), 500
    
# GET single hero by ID
@app.route('/api/heroes/<int:hero_id>' , methods=['GET'])
def get_hero(hero_id):
    try:
        cur = mysql.connection.cursor()
        # SQL query to get ONE hero by ID
        cur.execute("""
            SELECT h.*, a.attribute_type, r.role_name 
            FROM hero h
            LEFT JOIN attribute a ON h.ATTRIBUTE_attribute_id = a.attribute_id
            LEFT JOIN role r ON h.ROLE_role_id = r.role_id
            WHERE h.hero_id = %s
        """, (hero_id,))  # %s is a placeholder, hero_id goes here
        
        # Get the result, fetchone 
        hero = cur.fetchone()
        cur.close()
        
        # If hero not found handling
        if not hero:
            return jsonify({
                'success': False,
                'error': 'Hero not found'
            }), 404  # 404 = Not Found
        
        # Convert to dictionary
        hero_data = {
            'hero_id': hero[0],
            'hero_name': hero[1],
            'attack_type': hero[2],
            'attribute_id': hero[3],
            'role_id': hero[4],
            'attribute_type': hero[5] if len(hero) > 5 else None,
            'role_name': hero[6] if len(hero) > 6 else None
        }
        
        # Return success response
        return jsonify({
            'success': True,
            'data': hero_data
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    
# POST Create new hero
# Body: {"hero_name": "testname", "attack_type": "Melee/Ranged", "attribute_id": 1, "role_id": 2}
@app.route('/api/heroes', methods=['POST'])
def create_hero():
    try:
        # Get JSON data from request body
        data = request.get_json()
        
        # Check if data is empty, none or false
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400 
        
        # Get values from JSON
        hero_name = data.get('hero_name')
        attack_type = data.get('attack_type')
        attribute_id = data.get('attribute_id')
        role_id = data.get('role_id')
        
        # Validate required fields
        if not hero_name or not attack_type:
            return jsonify({
                'success': False,
                'error': 'hero_name and attack_type are required'
            }), 400
        
        # Validate hero name length, max 50
        if len(hero_name) > 50:
            return jsonify({
                'success': False,
                'error': 'hero_name must be 50 characters or less'
            }), 400
        
        # Ranged/Melee max 6
        if len(attack_type) > 10:
            return jsonify({
                'success': False,
                'error': 'attack_type must be 45 characters or less'
            }), 400
        
        # Insert into database
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO hero (hero_name, attack_type, ATTRIBUTE_attribute_id, ROLE_role_id)
            VALUES (%s, %s, %s, %s)
        """, (hero_name, attack_type, attribute_id, role_id))
        
        # Commit changes to db
        mysql.connection.commit()
        
        # Get last record id
        new_hero_id = cur.lastrowid
        cur.close()
        
        # Return success response
        return jsonify({
            'success': True,
            'message': 'Hero created successfully',
            'data': {
                'hero_id': new_hero_id,
                'hero_name': hero_name,
                'attack_type': attack_type,
                'attribute_id': attribute_id,
                'role_id': role_id
            }
        }), 201  # CREATED
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
