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

@app.route('/mock-tests')
def mock_tests_page():
    return render_template('mock-tests.html')

@app.route('/front-end-mock')
def front_end_mock_page():
    global questions 
    questions = questions_front_end
    return render_template('front-end-mock.html', questions = questions)

@app.route('/back-end-mock')
def back_end_mock_page():
    global questions 
    questions = questions_back_end
    return render_template('back-end-mock.html', questions = questions)

@app.route('/cybersecurity-mock')
def cybersecurity_mock_page():
    global questions 
    questions = questions_cyber
    return render_template('cybersecurity-mock.html', questions = questions)

@app.route('/Dev-Ops-mock')
def Dev_Ops_mock_page():
    global questions 
    questions = questions_dev_ops
    return render_template('Dev-Ops-mock.html', questions = questions)

@app.route('/submit', methods=['POST'])
def submit():
    responses = request.form
    score = 0
    total_marks = sum(q['marks'] for q in questions)

    # Iterate through questions to calculate the score
    for question in questions:
        question_id = str(question['id'])  # Ensure IDs are strings
        if question_id in responses:  # Check if the user responded
            user_answer = responses[question_id].strip()
            if 'answer' in question and user_answer == question['answer']:
                score += question['marks']  # Add marks for correct answers
            elif 'expected_answer' in question:
                # Example check for descriptive answers (simple check)
                if question['expected_answer'].lower() in user_answer.lower():
                    score += question['marks']  # Add marks for matching descriptive answers

    # Pass the score and total_marks to the results page
    return render_template("results.html", score=score, total_marks=total_marks)

@app.route('/results')
def show_results():
    # This route can be used for redirection if needed.
    return redirect(url_for('index'))


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
