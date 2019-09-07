from flask import Flask, render_template, request, json
import APImain
import main_functions
import os
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
    main_functions.save_to_file(userQuery, 'query.json');
    newQuery = main_functions.read_from_file("query.json")
    APImain.query(newQuery)
    json1 = "results_json0.json"
    myData = main_functions.read_from_file(json1)
    #userData= myData["organic"][5]["url"]
    return render_template('about.html', myData=myData)


#Debug mode is turned on
if __name__ == "__main__":
    app.run(debug=True)
