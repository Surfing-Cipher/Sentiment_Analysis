# 🧠 Sentiment Analysis Flask App [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Hk4JXwBJHod5Nu3jI3KW1tr22HRBXce0?usp=sharing)

A **Flask-based web application** that performs real-time sentiment analysis on product reviews using:

- **SentenceTransformer** (`all‑MiniLM‑L6‑v2`) for text embeddings
- **Logistic Regression** model for sentiment classification
- A polished **Bootstrap UI** with light/dark modes and loading spinner

---

## 📂 Project Structure

```
Sentiment-api/
├── app.py                  # Main Flask server
├── logistic_model.pkl     # Pre-trained sentiment classification model
├── templates/
│   └── index.html         # Web UI with Bootstrap, dark-mode toggle, and spinner
├── requirements.txt       # Python dependencies
└── .gitignore             # Ignore virtual environments, cache, PKL, etc.
```

---

## 🚀 How to Download & Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Surfing-Cipher/Sentiment_Analysis.git
cd Sentiment_Analysis
```

### 2. Configure environment (Python 3.8+ recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to access the UI.

---

## 🎯 Features

- **Real-time sentiment analysis** using pretrained Logistic Regression + embeddings
- **Responsive Bootstrap UI** with clean card-style layout
- Switch between **light/dark modes** for eye comfort
- **Loading spinner** for instant feedback during prediction
- Pastel background gradient for better readability
- Error handling and user-friendly messages

---

## 🛠️ File Descriptions

- **app.py** – Defines `/` route for the UI and `/predict` route for API
- **logistic_model.pkl** – Trained sklearn model for sentiment (+ model version handling)
- **index.html** – Web interface with toggle and spinner
- **requirements.txt** – Python dependencies (`Flask`, `sentence-transformers`, `scikit-learn`, `gunicorn`, etc.)

---

## 🔧 Deployment

To deploy (e.g. on Render.com):

1. Include `requirements.txt`
2. Use `gunicorn` in your start command:

```bash
gunicorn app:app
```

3. Set environment variables if needed, push to GitHub, and connect repo to Render.

---

## 👍 Next Enhancements

- Add **confidence scores** from `model.predict_proba`
- Save user feedback via a simple CSV or Google Sheets integration
- Add deployment badges (CI/CD, code coverage)
- Tweak **README** to include app screenshots (light/dark mode)

---

## 📝 Example Usage

![Light Mode Example](screenshots/light_mode.png)
![Dark Mode Example](screenshots/dark_mode.png)

```html
<button onclick="analyze()">Analyze Sentiment</button>
```

Yields:

```
Sentiment: Positive ✅
```

---

## 🤝 Contributing

- Feel free to open issues or PRs if you encounter bugs or want feature suggestions
- Please follow the existing **Bootstrap UI style** and **dark mode conventions**
