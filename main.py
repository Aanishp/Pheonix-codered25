# from flask import Flask, render_template

# #My db connection 
# local_server = True
# app = Flask(__name__)
# app.secret_key='15082003'

# #for home page
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/welcome')
# def welcome_page():
#     return render_template('welcome.html')

# @app.route('/services')
# def services_page():
#     return render_template('services.html')

# @app.route('/roadmap')
# def roadmap_page():
#     return render_template('roadmap.html')

# @app.route('/front-end')
# def front_end_page():
#     return render_template('front-end.html')

# @app.route('/back-end')
# def back_end_page():
#     return render_template('back-end.html')

# @app.route('/cybersecurity')
# def cybersecurity_page():
#     return render_template('cybersecurity.html')

# @app.route('/Dev-Ops')
# def dev_Ops_page():
#     return render_template('Dev-Ops.html')

# @app.route('/about')
# def about_page():
#     return render_template('about.html')

# @app.route('/sign-up')
# def sign_page():
#     return render_template('sign-up.html')

# @app.route('/contact')
# def contact_page():
#     return render_template('contact.html')

# @app.route('/project-ideas')
# def project_ideas_page():
#     return render_template('preject_ideas.html')

# @app.route('/age-calculator')
# def age_calculator_page():
#     return render_template('age-calculator.html')

# @app.route('/flash-cards')
# def flash_cards_page():
#     return render_template('flash-cards.html')

# @app.route('/pomodoro-timer')
# def pomodoro_timer_page():
#     return render_template('pomodoro-timer.html')

# @app.route('/weather-web-app')
# def weather_web_app_page():
#     return render_template('weather-web-app.html')

# @app.route('/expense-tracker-api')
# def expense_tracker_api_page():
#     return render_template('expense-tracker-api.html')

# @app.route('/tmbd-cli-tool')
# def tmbd_cli_tool_page():
#     return render_template('tmbd-cli-tool.html')

# @app.route('/workout-tracker')
# def workout_tracker_page():
#     return render_template('workout-tracker.html')

# @app.route('/image-processing-service')
# def image_processing_service_page():
#     return render_template('image-processing-service.html')

# app.run(debug=True)

## New code

from flask import Flask, render_template, request, redirect, url_for
from  questions import questions_dev_ops, questions_back_end, questions_cyber, questions_front_end

# Initialize Flask application
app = Flask(__name__)
app.secret_key = '15082003'

# Static Pages Routes
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

@app.route('/sign-up')
def sign_page():
    return render_template('sign-up.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/project_ideas')
def project_ideas_page():
    return render_template('project_ideas.html')

@app.route('/age-calculator')
def age_calculator_page():
    return render_template('age-calculator.html')

@app.route('/flash-cards')
def flash_cards_page():
    return render_template('flash-cards.html')

@app.route('/pomodoro-timer')
def pomodoro_timer_page():
    return render_template('pomodoro-timer.html')

@app.route('/weather-web-app')
def weather_web_app_page():
    return render_template('weather-web-app.html')

@app.route('/expense-tracker-api')
def expense_tracker_api_page():
    return render_template('expense-tracker-api.html')

@app.route('/tmbd-cli-tool')
def tmbd_cli_tool_page():
    return render_template('tmbd-cli-tool.html')

@app.route('/workout-tracker')
def workout_tracker_page():
    return render_template('workout-tracker.html')

@app.route('/image-processing-service')
def image_processing_service_page():
    return render_template('image-processing-service.html')

# @app.route('/image-processing-service')
# def image_processing_service_page():
#     return render_template('image-processing-service.html')

# Quiz/Test Functionality
# questions = [
#     {"id": 1, "question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Text Machine Language", "Hyperlink and Text Markup Language", "Home Tool Markup Language"], "answer": "Hyper Text Markup Language", "marks": 1},
#     {"id": 2, "question": "Which HTML tag is used to define an unordered list?", "options": ["<ul>", "<ol>", "<li>", "<list>"], "answer": "<ul>", "marks": 1},
#     {"id": 3, "question": "What does CSS stand for?", "options": ["Cascading Style Sheets", "Creative Style System", "Computer Style Sheets", "Colorful Style Sheets"], "answer": "Cascading Style Sheets", "marks": 1},
#     {"id": 4, "question": "Which CSS property is used to make the text bold?", "options": ["font-weight", "font-style", "text-decoration", "font-bold"], "answer": "font-weight", "marks": 2},
#     {"id": 5, "question": "What is the correct syntax to include an external JavaScript file in HTML?", "options": ["<script src='file.js'></script>", "<script href='file.js'></script>", "<script link='file.js'></script>", "<script url='file.js'></script>"], "answer": "<script src='file.js'></script>", "marks": 2},
#     {"id": 6, "question": "Which JavaScript method is used to add an event listener to an element?", "options": ["addEventListener()", "attachEvent()", "onEvent()", "setEventListener()"], "answer": "addEventListener()", "marks": 3},
#     {"id": 7, "question": "Which HTML5 element is used to define navigation links?", "options": ["<nav>", "<menu>", "<navbar>", "<navigation>"], "answer": "<nav>", "marks": 3},
#     {"id": 8, "question": "Explain the box model in CSS and how 'box-sizing' affects it.", "expected_answer": "The box model in CSS consists of margins, borders, padding, and the actual content. The 'box-sizing' property defines whether the width and height include padding and border or not.", "marks": 5},
#     {"id": 9, "question": "Describe how Flexbox works in CSS and provide examples of its key properties.", "expected_answer": "Flexbox is a CSS layout model that provides an efficient way to align and distribute space among items in a container, even when their sizes are dynamic.", "marks": 5}
# ]

@app.route('/quiz')
def quiz_page():
    return render_template('qu.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    responses = request.form
    score = 0
    total_marks = sum(q['marks'] for q in questions)

    for question in questions:
        if str(question['id']) in responses:
            if question.get('answer') and responses[str(question['id'])] == question['answer']:
                score += question['marks']
            elif question.get('expected_answer'):
                user_answer = responses[str(question['id'])].strip()
                if len(user_answer) > 20:  # Example check
                    score += question['marks']

    return render_template('test.html', questions=questions, score=score, total_marks=total_marks)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
