from flask import Flask, render_template, request, json
import os
import main_functions
app = Flask(__name__)

#Adds home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/serialize', methods=['POST'])
def serialize():
    userQuery = request.form['query'];
    return json.dumps({'keyword': userQuery});


#Debug mode is turned on
if __name__ == "__main__":
    app.run(debug=True)
