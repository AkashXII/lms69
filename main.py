from fastapi import FastAPI
import psycopg2

app = FastAPI()

db_url = "postgresql://adithya:ZOCO9pbKeDQye6atTuN76D7CptIBuiCi@dpg-cvt4svi4d50c73dedpqg-a.oregon-postgres.render.com/lms_db_54b3"

@app.get("/")
def home_route():
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s);", ("adithya", 25))
    conn.commit()
    
    cursor.close()
    conn.close()

    return {"message": "successful"}