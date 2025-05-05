from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

class Customer(BaseModel):
    cust_id: int
    cust_name: str
    address: str
    phone_no: str

class Employee(BaseModel):
    e_id: int
    emp_name: str
    address: str
    phone_no: str

class Book(BaseModel):
    book_id: int
    publisher: str
    title: str
    num_copies: int
    availability: bool

class BookIssue(BaseModel):
    
    c_id: int
    book_id: int
    e_id: int
    money: float  # Format: 'YYYY-MM-DD'
    days: int 

db_url = "postgresql://postgres.gdzstvmbarrkrdqgkfkw:dN50aW3qXVtpfsjR@aws-0-us-east-2.pooler.supabase.com:6543/postgres"

@app.get("/customer")
def home_route():
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()
    
    cursor.execute("select * from customer;")
    rows=cursor.fetchall()
    conn.commit()
    
    cursor.close()
    conn.close()

    return {"message": rows}

@app.get("/employee")
def home_route():
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()
    
    cursor.execute("select * from employee;")
    rows=cursor.fetchall()
    conn.commit()
    
    cursor.close()
    conn.close()

    return {"message": rows}

@app.get("/book")
def home_route():
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()
    
    cursor.execute("select * from book b join book_details bd on b.book_id=bd.book_id;")
    rows=cursor.fetchall()
    conn.commit()
    
    cursor.close()
    conn.close()

    return {"message": rows}

@app.get("/fine")
def home_route():
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()
    
    cursor.execute("select * from fine join customer on fine.c_id=customer.c_id;")
    rows=cursor.fetchall()
    conn.commit()
    
    cursor.close()
    conn.close()

    return {"message": rows}

@app.post("/add_customer")
def add_customer(customer: Customer):
    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO customer (cust_id, cust_name, address, phone_no) VALUES (%s, %s, %s, %s)",
            (customer.cust_id, customer.cust_name, customer.address, customer.phone_no)
        )
        conn.commit()
        return {"message": "Customer added successfully"}
    except Exception as e:
        return {"message": f"Error: {e}"}
    finally:
        cursor.close()
        conn.close()

@app.post("/add_employee")
def add_employee(emp: Employee):
    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employee (e_id, emp_name, address, phone_no) VALUES (%s, %s, %s, %s)",
            (emp.e_id, emp.emp_name, emp.address, emp.phone_no)
        )
        conn.commit()
        return {"message": "Employee added successfully"}
    except Exception as e:
        return {"message": f"Error: {e}"}
    finally:
        cursor.close()
        conn.close()

@app.post("/add_book")
def add_book(book: Book):
    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO book (book_id, publisher, title, num_copies, availability) VALUES (%s, %s, %s, %s)",
            (book.book_id, book.publisher, book.title, book.num_copies, book.availability )
        )
        conn.commit()
        return {"message": "Book added successfully"}
    except Exception as e:
        return {"message": f"Error: {e}"}
    finally:
        cursor.close()
        conn.close()

@app.post("/add_book_issue")
def add_book_issue(issue: BookIssue):
    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO book_details (c_id,book_id, e_id,money, days) VALUES (%s, %s, %s, %s, %s)",
            (issue.c_id, issue.book_id, issue.e_id,issue.money,issue.days)
        )
        conn.commit()
        return {"message": "Book issue recorded successfully"}
    except Exception as e:
        return {"message": f"Error: {e}"}
    finally:
        cursor.close()
        conn.close()

    

    