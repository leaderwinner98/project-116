# importing modules from flask library
from flask import Flask, render_template

# creating an instance of class Flask, by providing __name__ keyword as an argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():
    name = "Priyam"  # write your name
    age = "15"   # write your age
    return render_template('index.html', name=name, age=age)

# define the route to father webpage
@app.route("/father")
def father():
    # Add any specific data or logic for the father webpage
    return render_template('father.html')

# define the route to mother webpage
@app.route("/mother")
def mother():
    # Add any specific data or logic for the mother webpage
    return render_template('mother.html')

# define the route to friends webpage
@app.route("/friends")
def friends():
    # Add any specific data or logic for the friends webpage
    return render_template('friends.html')

# add other routes, if you want

# run the file
if __name__ == '__main__':
    app.run(debug=True)
