from flask import Flask, render_template, request, jsonify
from models.financial_advice_model import generate_financial_advice

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_advice', methods=['POST'])
def get_advice():
    user_input = request.json.get('user_input')
    response = generate_financial_advice(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
