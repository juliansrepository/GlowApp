from flask import Flask, render_template

app = Flask(__name__)

#Adds home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

#Adds about page
@app.route('/about')
def about():
    return render_template('about.html')

#Debug mode is turned on
if __name__ == "__main__":
    app.run(debug=True)
