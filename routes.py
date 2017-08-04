from flask import Flask, render_template

app=Flask(__name__)


@app.route('/<name>')
def hello(name):
	return render_template("index.html",userName=name)

#@app.route('/user/<int:age>')
#def user_age(age):
#    return "<h1>Age of user is: %d</h1>"%age

#@app.route('/user/<name>')
#def user_name(name):
#    return render_template("index.html",userName=name)
	
if __name__=="__main__":
	app.run(debug=True)