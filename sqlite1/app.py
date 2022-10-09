from flask import Flask, render_template, request
app=Flask(__name__)
import sqlite3 as sql

@app.route('/')
def home():
    return "Welcome to Home Page"

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/insert',methods=['POST','GET'])
def insert():
    if(request.method=='POST'):
        try:
            name=request.form['name']
            age=request.form['age']
            city=request.form['city']
            course=request.form['course']

            with sql.connect('database.db') as con:
                cur=con.cursor()
                cur.execute("INSERT INTO students (name,age,city,course) VALUES (?,?,?,?)",(name,age,city,course))
                con.commit()
                msg="SUCCESS"
        except:
            con.rollback()
            msg="ERROR"
        finally:
            con.close()
            return render_template('result.html',msg=msg)

@app.route('/display')
def display():
    con=sql.connect("database.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from students")
    rows=cur.fetchall()
    return render_template('display.html',rows=rows)
@app.route('/delete/<name>')
def delete(name):
    con=sql.connect("database.db")
    con.execute("DELETE from students where name=?",[name])
    con.commit()
    print("Deleted Successfully")
    con.close()
    return render_template('display.html')

if(__name__=="__main__"):
    app.run(debug=True)
            


