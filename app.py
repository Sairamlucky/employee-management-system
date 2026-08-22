from flask import Flask,render_template,request,redirect,url_for
import psycopg

app = Flask(__name__)
@app.route("/")
def home():
    return "Hello sai!Welcome to flask"

@app.route("/about")
def about():
    return "this is another page"

@app.route("/employees")
def employees():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM employees")
    employees=cur.fetchall()

    return render_template("employees.html",employees = employees)

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

@app.route("/employees/create",methods=["POST"])
def create_employee():
    name =request.form["name"]
    email =request.form["email"]

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
    "INSERT INTO employees(name,email) VALUES(%s,%s)",
    (name,email)
    )

    conn.commit()

    cur.close()
    conn.close()

    return "The employee created suceesfully"

def get_db_connection():
    conn = psycopg.connect( 
        host = 'localhost',
        port = 5432,
        dbname = "employee_db",
        user = "postgres",
        password = "Postgres@123"
    )
    return conn
conn = get_db_connection()
print("database connected sucessfully")
conn.close()


if __name__ == "__main__":
    app.run(debug=True)