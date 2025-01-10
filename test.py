from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask('__name__')

# Sample questions
questions = [
    {"id": 1, "question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Text Machine Language", "Hyperlink and Text Markup Language", "Home Tool Markup Language"], "answer": "Hyper Text Markup Language", "marks": 1},
    {"id": 2, "question": "Which CSS property is used to make the text bold?", "options": ["font-weight", "font-style", "text-decoration", "font-bold"], "answer": "font-weight", "marks": 2},
    {"id": 3, "question": "Which JavaScript method is used to add an event listener to an element?", "options": ["addEventListener()", "attachEvent()", "onEvent()", "setEventListener()"], "answer": "addEventListener()", "marks": 3},
    {"id": 4, "question": "Explain the box model in CSS and how 'box-sizing' affects it.", "expected_answer": "The box model consists of margins, borders, padding, and content. 'box-sizing' controls whether padding and border are included in width/height.", "marks": 5}
]

@app.route('/')
def index():
    return render_template('test.html', questions=questions)

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
                # Basic scoring for descriptive answers
                user_answer = responses[str(question['id'])].strip()
                if len(user_answer) > 20:  # Example check
                    score += question['marks']

    print({"score": score, "total_marks": total_marks})

    return render_template("test.html", questions=questions)

app.run(debug=True)