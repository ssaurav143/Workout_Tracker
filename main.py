import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")

USERNAME = os.getenv("SHEETY_USERNAME")
PASSWORD = os.getenv("SHEETY_PASSWORD")

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32

base_url = "https://app.100daysofpython.dev"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

posting_endpoint = f"{base_url}/v1/nutrition/natural/exercise"

posting_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=posting_endpoint, json=posting_params, headers=headers)

result = response.json()
print(result["exercises"])

sheety_base_url = "https://api.sheety.co/da72d1b4cdaca4eeb19b1fa4a75380b8/workoutTracking/workouts"

sheety_base_response = requests.get(url=sheety_base_url, auth=(USERNAME, PASSWORD))
sheety_base_result = sheety_base_response.json()
print(sheety_base_result)
print(f"Nutritionix API call: \n {sheety_base_result} \n")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GOOGLE_SHEET_NAME = "workout"

sheety_posting_url = "https://api.sheety.co/da72d1b4cdaca4eeb19b1fa4a75380b8/workoutTracking/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_posting_response = requests.post(
        sheety_posting_url,
        json=sheet_inputs,
        auth=(USERNAME, PASSWORD)
    )

    print(f"Sheety Response: \n {sheety_posting_response.text}")