# mock_data_generator.py

import json
import random
from datetime import datetime, timedelta

def generate_flight_data(num_entries=100):
    flights = []
    for i in range(num_entries):
        flight = {
            "flight_number": f"FL{random.randint(1000, 9999)}",
            "departure_airport": random.choice(["JFK", "LAX", "ORD", "DFW", "ATL"]),
            "arrival_airport": random.choice(["JFK", "LAX", "ORD", "DFW", "ATL"]),
            "departure_time": (datetime.now() + timedelta(minutes=random.randint(10, 180))).isoformat(),
            "arrival_time": (datetime.now() + timedelta(minutes=random.randint(180, 360))).isoformat(),
            "status": random.choice(["On Time", "Delayed", "Cancelled"])
        }
        flights.append(flight)
    return flights

def save_mock_data(filename='mock_flight_data.json'):
    data = generate_flight_data()
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    save_mock_data()
