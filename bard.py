from flask import Flask, request, jsonify
from bardapi import Bard

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()

    if 'token' not in data or 'prompt' not in data:
        return jsonify({'error': 'Both token and prompt must be provided'}), 400

    token = data['token']
    question = data['prompt']

    bard = Bard(token=token)
    answer = bard.get_answer(question)
    if 'content' in answer:
        return jsonify({'answer': answer['content']})
    else:
        return jsonify({'error': 'No answer was found'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Allow connections from any external host
