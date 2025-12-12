from flask import Flask, jsonify
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

# 200 OK
# 404 NOT FOUND
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

if __name__ == '__main__':
    app.run(debug=True)
