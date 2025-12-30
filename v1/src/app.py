# app_vuln.py  (vulnerable a propósito)
import os
from dotenv import load_dotenv
import pyodbc
from flask import Flask, jsonify, request
from modules.database import Database 

from datetime import datetime

load_dotenv()

app = Flask(__name__)

CONN_STR = Database.build_conn_str(*eval(os.getenv("DBCONN")))
db_agent = Database(CONN_STR)

@app.route('/')
def index():
    if not db_agent or not db_agent.cursor:
        db_agent.connect()
        # return jsonify({"error": "DB no inicializada"}), 500
    
    try:
        id = request.args.get('id')
        c_where = f"WHERE id = {id}"
        
        sql = f"SELECT COUNT(*) FROM dbo.profiles {c_where};"
        
        db_agent.execute_query(sql)
        total = db_agent.cursor.fetchone()[0]

        return jsonify({"status": "ok", "profiles_total": total})
    except Exception as e:
        return jsonify({"error": e}), 500
    
@app.route('/2')
def index2():
    if not db_agent or not db_agent.cursor:
        db_agent.connect()
        # return jsonify({"error": "DB no inicializada"}), 500
    
    try:
        id = request.args.get('id')
        c_where = f"WHERE id = {id}"
        
        sql = f"SELECT COUNT(*) FROM dbo.profiles {c_where};"
        
        db_agent.execute_query(sql)
        total = db_agent.cursor.fetchone()[0]

        return jsonify({"status": "ok", "profiles_total": total})
    except Exception as e:
        return jsonify({"error": e}), 500