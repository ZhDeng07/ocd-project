from flask import Flask, request, jsonify, render_template
from gpt_utils import call_gpt  # 从gpt_utils导入GPT函数

app = Flask(__name__)

# Route to serve the index.html file
@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/api/gpt', methods=['POST'])
def gpt_chat():
    user_input = request.json.get('text')
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # 调用Prompt engineering的GPT函数
    gpt_response = call_gpt(user_input)
    
    if isinstance(gpt_response, dict) and "error" in gpt_response:
        return jsonify(gpt_response), 500

    return jsonify(gpt_response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)