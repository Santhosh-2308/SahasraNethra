from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from predict import predict_wildfire  # Import your ML function

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

@app.route('/ml-alerts', methods=['GET'])
def get_ml_alerts():
    """
    API endpoint to fetch the latest wildfire alert.
    """
    try:
        result = predict_wildfire()  # Get prediction result
        return jsonify({"type": "Wildfire Alert", "message": result, "link": "#"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle errors gracefully

if __name__ == "__main__":
    app.run(debug=True)
