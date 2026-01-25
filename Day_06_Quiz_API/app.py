from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Constants
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
QUESTIONS_FILE = os.path.join(DATA_DIR, 'questions.json')
RESULTS_FILE = os.path.join(DATA_DIR, 'results.json')

def load_questions():
    if not os.path.exists(QUESTIONS_FILE):
        return []
    with open(QUESTIONS_FILE, 'r') as f:
        return json.load(f)

def save_result(score):
    results = []
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r') as f:
            try:
                results = json.load(f)
            except json.JSONDecodeError:
                results = []
    
    results.append({'score': score})
    
    with open(RESULTS_FILE, 'w') as f:
        json.dump(results, f, indent=4)

@app.route('/api/questions', methods=['GET'])
def get_questions():
    questions = load_questions()
    # Hide the correct answer from the client
    questions_for_client = []
    for q in questions:
        q_copy = q.copy()
        if 'answer' in q_copy:
            del q_copy['answer']
        questions_for_client.append(q_copy)
    return jsonify(questions_for_client)

@app.route('/api/submit', methods=['POST'])
def submit_quiz():
    user_answers = request.json.get('answers', {})
    questions = load_questions()
    score = 0
    total = len(questions)
    
    for q in questions:
        q_id = str(q['id'])
        if q_id in user_answers and user_answers[q_id] == q['answer']:
            score += 1
            
    save_result(score)
    
    return jsonify({
        'score': score,
        'total': total,
        'message': f'You scored {score} out of {total}'
    })

if __name__ == '__main__':
    app.run(debug=True)
