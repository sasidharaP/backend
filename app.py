from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Route to check if the app is working
@app.route('/')
def home():
    return "Hello, Vercel! Your Flask app is live."

# API endpoint to demonstrate JSON response
@app.route('/api', methods=['GET'])
def api():
    return jsonify({
        'message': 'Welcome to the Python backend deployed on Vercel!',
        'status': 'success'
    })

# Vercel expects the Flask app to be callable directly without app.run()
if __name__ == '__main__':
    pass
