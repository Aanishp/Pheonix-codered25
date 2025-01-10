from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask('__name__')

# Sample questions
questions = [
    {"id": 1, "question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Text Machine Language", "Hyperlink and Text Markup Language", "Home Tool Markup Language"], "answer": "Hyper Text Markup Language", "marks": 1},
    {"id": 2, "question": "Which HTML tag is used to define an unordered list?", "options": ["<ul>", "<ol>", "<li>", "<list>"], "answer": "<ul>", "marks": 1},
    {"id": 3, "question": "What does CSS stand for?", "options": ["Cascading Style Sheets", "Creative Style System", "Computer Style Sheets", "Colorful Style Sheets"], "answer": "Cascading Style Sheets", "marks": 1},
    {"id": 4, "question": "Which CSS property is used to make the text bold?", "options": ["font-weight", "font-style", "text-decoration", "font-bold"], "answer": "font-weight", "marks": 2},
    {"id": 5, "question": "What is the correct syntax to include an external JavaScript file in HTML?", "options": ["<script src='file.js'></script>", "<script href='file.js'></script>", "<script link='file.js'></script>", "<script url='file.js'></script>"], "answer": "<script src='file.js'></script>", "marks": 2},
    {"id": 6, "question": "Which JavaScript method is used to add an event listener to an element?", "options": ["addEventListener()", "attachEvent()", "onEvent()", "setEventListener()"], "answer": "addEventListener()", "marks": 3},
    {"id": 7, "question": "Which HTML5 element is used to define navigation links?", "options": ["<nav>", "<menu>", "<navbar>", "<navigation>"], "answer": "<nav>", "marks": 3},
    {"id": 8, "question": "Explain the box model in CSS and how 'box-sizing' affects it.", "expected_answer": "The box model in CSS consists of margins, borders, padding, and the actual content. The 'box-sizing' property defines whether the width and height include padding and border or not.", "marks": 5},
    {"id": 9, "question": "Describe how Flexbox works in CSS and provide examples of its key properties.", "expected_answer": "Flexbox is a CSS layout model that provides an efficient way to align and distribute space among items in a container, even when their sizes are dynamic.", "marks": 5}
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