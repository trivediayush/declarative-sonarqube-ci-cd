from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            dbname="sample",
            user="user",
            password="pass",
            host="db",
            port="5432"
        )
        return "Connected to DB! Environment provisioned.", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
