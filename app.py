#!python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST']) #decorator to specify: if you visit the website at root, you will get this message
def rootpage():
    name = ''
    food = ''
    if request.method == 'POST' and 'name_input' in request.form:
    #If there's a post request, and it contains name input in the form, take data from the name input and assign to the variable
        name = request.form.get('name_input')
        food = request.form.get('food_input')
    return render_template('index.html',name=name, food=food #We are giving name variable to name in index.html
    )


app.run()