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

@app.route('/roadmap')
def roadmap_page():
    return render_template('roadmap.html')

@app.route('/front-end')
def front_end_page():
    return render_template('front-end.html')

@app.route('/back-end')
def back_end_page():
    return render_template('back-end.html')

@app.route('/cybersecurity')
def cybersecurity_page():
    return render_template('cybersecurity.html')

@app.route('/Dev-Ops')
def dev_Ops_page():
    return render_template('Dev-Ops.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

app.run(debug=True)