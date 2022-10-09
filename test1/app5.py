from flask import Flask, render_template
app=Flask(__name__)

@app.route('/hello/<int:score>')
def score(score):
    return render_template('index.html',marks=score)

if(__name__=='__main__'): 
    app.run(debug=True)

