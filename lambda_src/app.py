import json
import os
import pymysql

def get_connection():
    return pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        connect_timeout=5,
        cursorclass=pymysql.cursors.DictCursor
    )

def lambda_handler(event, context):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            # Crea la tabla si no existe
            cursor.execute("CREATE TABLE IF NOT EXISTS items (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100))")
            
            # Cuenta los registros
            cursor.execute("SELECT COUNT(*) AS total FROM items")
            result = cursor.fetchone()
            total = result["total"]
            
        conn.commit()
        conn.close()
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Lambda conectada correctamente a RDS MySQL",
                "items_registrados": total
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }