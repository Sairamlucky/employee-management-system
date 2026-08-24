from flask import Flask,render_template,request,redirect,url_for,flash
import psycopg
import os
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()

app.secret_key = os.getenv("FLASK_SECRET_KEY")
@app.route("/")
def home():

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM employees")
    total_employees = cur.fetchone()[0]

    cur.close()
    conn.close()

    return render_template(
        "dashboard.html",
        total_employees=total_employees
    )
@app.route("/about")
def about():
    return "this is another page"

@app.route("/employees")
def employees():
    search = request.args.get("search","").strip()

    conn = get_db_connection()
    cur = conn.cursor()

    if search:
        cur.execute(
            """SELECT * FROM employees 
               WHERE name ILIKE %s
               or email ILIKE  %s
               ORDER BY id
            """,
            (f"%{search}%",f"%{search}%")
        )
    else:
        cur.execute(

            "SELECT * FROM employees ORDER BY id"
        )

    employees=cur.fetchall()
    cur.close()
    conn.close()

    return render_template("employees.html",employees = employees,search = search)

@app.route("/employees/create",methods = ["GET"])
def create_employee_page():

    return render_template("employee.html")

@app.route("/employees/edit/<int:id>", methods =["GET","POST"])
def edit_employee(id):

    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        cur.execute(
            "UPDATE employees SET name = %s, email = %s WHERE id = %s",
            (name, email, id)
        )

        conn.commit()

        cur.close()
        conn.close()

        return redirect(url_for("employees"))

    cur.execute(
        "SELECT * FROM employees WHERE id = %s",
        (id,)
    )

    employee = cur.fetchone()

    cur.close()
    conn.close()

    return render_template("edit_employee.html", employee=employee)
@app.route("/employees/view/<int:id>")
def view_employee(id):

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM employees WHERE id = %s",
        (id,)
    )

    employee = cur.fetchone()

    cur.close()
    conn.close()

    if employee is None:
        return "Employee not found", 404

    return render_template("view_employee.html",employee=employee
    )
@app.route("/employees/delete/<int:id>")
def delete_employee(id):

    conn = get_db_connection()
    cur  = conn.cursor()

    cur.execute (
        "DELETE FROM employees WHERE id = %s",
        (id ,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for("employees"))

@app.route("/employees/create", methods=["POST"])
def create_employee():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()

    # Empty field validation
    if not name or not email:
        flash("Name and email are required.", "error")
        return redirect(url_for("create_employee_page"))

    # Name validation
    if len(name) < 2:
        flash("Employee name must contain at least 2 characters.", "error")
        return redirect(url_for("create_employee_page"))

    # Email validation
    if "@" not in email or "." not in email:
        flash("Please enter a valid email address.", "error")
        return redirect(url_for("create_employee_page"))

    conn = None
    cur = None

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO employees (name, email) VALUES (%s, %s)",
            (name, email)
        )

        conn.commit()

        flash("Employee created successfully!", "success")

    except Exception as e:

        if conn:
            conn.rollback()

        print("Database error:", e)

        flash("Unable to create employee. Please try again.", "error")

    finally:

        if cur:
            cur.close()

        if conn:
            conn.close()

    return redirect(url_for("employees"))

def get_db_connection():
    conn = psycopg.connect( 
        host = os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn
conn = get_db_connection()
print("database connected sucessfully")
conn.close()


if __name__ == "__main__":
    app.run(debug=True)