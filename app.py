import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Configure API key - it's better to use environment variables
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash-latest')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_google_ai():
    user_input = request.json.get('text')
    
    try:
        # Call the generative model
        response = model.generate_content(user_input)
        
        # Return the generated text
        return jsonify({"output": response.text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)