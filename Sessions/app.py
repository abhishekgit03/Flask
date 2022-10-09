from flask import Flask, session, redirect, url_for, escape, request
app=Flask(__name__)
app.secret_key="od234flu542djf345w65oe"

@app.route('/')
def index():
    if 'username' in session:
        username=session['username']
        return "Logged in as "+username
    return 'You are not logged in'
    
@app.route('/login', methods = ["POST", "GET"])
def login():
   if request.method == "POST":
      session['username'] = request.form.get('username')
      return redirect(url_for('index'))
   return '''
	
   <form action = "" method = "post">
      <p>Enter name <input type ="text" name = "username"/></p>
      <p><input type = "submit" value = "Login"/></p>
   </form>
	
   '''
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

if(__name__=='__main__'):
    app.run(debug=True)