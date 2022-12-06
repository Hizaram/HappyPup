#!/usr/bin/python3
"""Flask application for the HappyPup project"""

from flask import Flask, render_template, session, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL
from models.owner import Owner
from flask_session import Session
import json
from models import storage

app = Flask(__name__)
app.config.from_pyfile('config.py')

mysql = MySQL(app)
Session(app)

@app.route("/")
def hello_index():
    return render_template("0-index.html")

@app.route("/login.html")
def hello_login():
    return render_template("login.html")

@app.route("/register.html")
def hello_register():
    return render_template("register.html")

@app.route("/app.py", methods=['GET', 'POST'])
def login():
    """Defines the form logic, querying the database and validating
    user input"""
    if 'login' in request.form:
        if request.method == 'POST':
            o_email= request.form['email']
            o_password = request.form['password']
            try:
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM owners WHERE email=%s AND password=%s;",
                            [o_email, o_password])
                res = cur.fetchone()

                if res:
                    session['fname'] = res[6] + " " + res[7]
                    session['email'] = res[3]
                    session['phone'] = res[5]
                    session['id'] = res[0]
                    return redirect(url_for("dashboard"))
                else:
                    return render_template('0-index.html')
            except Exception as e:
                print (e)

            finally:
                mysql.connection.commit()
                cur.close()

    elif 'register' in request.form:
        if request.method == 'POST':
            fname = request.form['firstname']
            lname = request.form['lastname']
            phone = request.form['phonenumber']
            email = request.form['email']
            password = request.form['password']
            content = {"fname":str(fname), "lname":str(lname),
                       "phone":str(phone), "email":str(email),
                       "password":str(password)}

            if type(content) is dict:
                if "fname" in content.keys():
                    owner = Owner(**content)
                    storage.new(owner)
                    storage.save
                    o_dict = owner.to_dict()
                    response = jsonify(o_dict)
                    id = o_dict["id"]
                    c_at = o_dict['created_at']
                    u_at = o_dict['updated_at']
                    fname = o_dict['fname']
                    lname = o_dict['lname']
                    phone = o_dict['phone']
                    password = o_dict['password']
                    cur = mysql.connection.cursor()
                    cur.execute("INSERT into owners (id, created_at, updated_at, email, password, phone, fname, lname) values(%s, %s, %s, %s, %s, %s, %s, %s);",
                                [id, c_at, u_at, email, password, phone, fname, lname])
                    response.status_code = 201
                    mysql.connection.commit()
                    cur.close()
                    #return response
                    return redirect(url_for("hello_login"))
                else:
                    error_message = "Missing name"
            else:
                error_message = "Not a JSON"
        response = jsonify({'error': error_message})
        response.status_code = 400
        return response

    return render_template("0-index.html")

@app.route("/dashboard.html", methods=['GET', 'POST'])
def dashboard():
    """Displays the information needed for the dashboard including
    the owner details and dog details"""
    return render_template("dashboard.html")

@app.route("/logout.html")
def logout():
    """Redirects back to the home page and ends the session"""
    session.clear()
    return redirect(url_for("hello_index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
