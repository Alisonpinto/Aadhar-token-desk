from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS
import mysql.connector
import os

app = Flask(_name_)
CORS(app)

# MySQL Config - Now using environment variables
db_config = {
    'host': os.getenv('MYSQLHOST'),
    'user': os.getenv('MYSQLUSER'),
    'password': os.getenv('MYSQLPASSWORD'),
    'database': os.getenv('MYSQLDATABASE'),
    'port': os.getenv('MYSQLPORT', '3306')
}

# Update your db_config in app.py to include error handling:
db_config = {
    'host': os.getenv('MYSQLHOST', 'localhost'),
    'user': os.getenv('MYSQLUSER', 'root'),
    'password': os.getenv('MYSQLPASSWORD', ''),
    'database': os.getenv('MYSQLDATABASE', 'Aadhar Card'),
    'port': os.getenv('MYSQLPORT', '3306')
}

# Add this before your routes to test connection
@app.before_first_request
def test_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        conn.close()
        print("✅ Database connection successful")
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")

# Route to store signup data
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'message': 'Missing data'}), 400
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(sql, (name, email))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'User added successfully'})

    except mysql.connector.Error as err:
        return jsonify({'message': f'Error: {err}'}), 500

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
