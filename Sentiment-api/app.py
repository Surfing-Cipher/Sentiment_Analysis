from flask import Flask, request, jsonify, render_template
from sentence_transformers import SentenceTransformer
import joblib

app = Flask(__name__)

# Load logistic regression model and embedder
model = joblib.load("logistic_model.pkl")  # Trained model
embedder = SentenceTransformer('all-MiniLM-L6-v2')  # CPU-friendly embedder

print("✅ Model and embedder loaded successfully.")

@app.route('/')
def home():
    return render_template('index.html')  # Make sure index.html exists in /templates

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data.get("review", "")

    # Basic preprocessing
    review_clean = review.lower()

    # Convert to embedding
    embedding = embedder.encode([review_clean])

    # Predict sentiment
    prediction = model.predict(embedding)[0]
    sentiment = "Positive" if prediction == 1 else "Negative"

    return jsonify({
        'review': review,
        'prediction': sentiment,
        'label': int(prediction)
    })

if __name__ == '__main__':
    app.run(debug=True)
