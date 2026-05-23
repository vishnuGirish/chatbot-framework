from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json['input']
    response = generate_response(user_input)
    return jsonify({'response': response})