# 🏋️ Workout Tracker

A Python application that allows users to log workouts using natural language. The project uses the Nutritionix API to analyze exercise information and automatically stores workout records in a Google Sheet through the Sheety API.

## 📌 Features

✅ Enter workouts in plain English

✅ Uses Nutritionix Natural Language Processing

✅ Calculates exercise duration and calories burned

✅ Automatically records workout data in Google Sheets

✅ Stores API credentials securely using environment variables

✅ Beginner friendly API integration project

---

## 🛠 Technologies Used

* Python
* Requests
* Nutritionix API
* Sheety API
* Google Sheets
* Python Dotenv

---

## 📂 Project Structure

```text
Workout_Tracker/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🚀 How It Works

1. User enters workout information in natural language.

Example:

```text
swam for 1 hour
```

2. Nutritionix analyzes the text and returns:

* Exercise name
* Duration
* Calories burned

3. The workout data is sent to Sheety.

4. Sheety updates the connected Google Sheet automatically.

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
NUTRITIONIX_APP_ID=your_app_id
NUTRITIONIX_API_KEY=your_api_key

SHEETY_USERNAME=your_username
SHEETY_PASSWORD=your_password
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Workout_Tracker.git
cd Workout_Tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

Example:

```text
Tell me which exercises you did:
swam for 1 hour
```

Output:

```text
Swimming
Duration: 60 minutes
Calories: 512
```

The workout will automatically be added to the connected Google Sheet.

---

## 🎯 Learning Outcomes

This project helped practice:

* REST APIs
* HTTP Requests
* Authentication
* Environment Variables
* JSON Handling
* Google Sheets Automation
* Python Automation

---

## 👨‍💻 Author

Satya Saurav

Built as part of the Python learning journey.
