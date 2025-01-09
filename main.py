from flask import Flask, render_template

#My db connection 
local_server = True
app = Flask(__name__)
app.secret_key='15082003'

#for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome_page():
    return render_template('welcome.html')

@app.route('/services')
def services_page():
    return render_template('services.html')

app.run(debug=True)