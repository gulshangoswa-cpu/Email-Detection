# 👑 Gulshan AI Mail Classifier

A complete production-ready AI SaaS project that intelligently classifies email subject lines using Machine Learning. Built with a premium, futuristic billionaire-tech aesthetic.

## 🚀 Features

- **Neural Classifier**: Real-time AI prediction of email subjects.
- **Dynamic Categories**: Spam, Promotion, Social, Personal, Work, Finance, Updates, Security, OTP, Important.
- **Premium Dashboard**: Glassmorphism UI, neon gradients, and Chart.js analytics.
- **Secure Authentication**: User registration and login via Flask-Login and Bcrypt.
- **History & Export**: View past predictions and download them as CSV.
- **Admin Panel**: Manage users and view platform analytics.
- **RESTful API**: External integration capabilities.

## 📸 Screenshots
*(Add your screenshots here)*
- **Landing Page**: Showcases the typing animation and premium dark mode.
- **Dashboard**: Displays the Neural Classifier and user stats.
- **History**: Shows the interactive datatable with confidence scores.

## 🛠️ Installation

### Prerequisites
- Python 3.10+
- Git

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gulshan-ai-mail.git
   cd gulshan-ai-mail
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the ML model:**
   Before running the app, you need to train the model using the provided dataset.
   ```bash
   python backend/ml/train.py
   ```
   *This will generate the required `classifier.pkl` file in the `trained_model` directory.*

5. **Run the application:**
   ```bash
   python app.py
   ```
   *The app will run at http://127.0.0.1:5000*

## 🐳 Deployment (Docker)

1. **Build the image:**
   ```bash
   docker build -t gulshan-ai .
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 -d gulshan-ai
   ```

## 🔌 API Documentation

You can use the API for external requests (Requires authentication).

**Endpoint:** `POST /api/predict`

**Headers:**
- `Content-Type: application/json`

**Request Body:**
```json
{
  "subject": "Win free iPhone now"
}
```

**Response:**
```json
{
  "category": "Spam",
  "confidence": "97.5%"
}
```

## 🔮 Future Improvements
- Implement JWT API authentication for stateless external requests.
- Add Model Retraining module within the admin panel.
- Implement email simulation to show live push notifications.
- Enable dark/light mode toggle based on user preferences.
- Create a public leaderboard for user engagement.

## 📄 License
MIT License - Developed for Gulshan AI.
