from flask import Flask
app=Flask(__name__)

@app.route('/')
def func():
    return 'Hello from Home Page'

@app.route('/<name>')
def namefunc(name):
    return "Hello %s this is your page" % name

@app.route('/about')
def aboutfunc():
    return "This is contact page"

if __name__=='__main__':
    app.run(debug=True)




