from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

@app.route('/')
def index():
    return jsonify({
        'message': 'Testing!',
        'database': 'finaldbcselec'
    })

if __name__ == '__main__':
    app.run(debug=True)