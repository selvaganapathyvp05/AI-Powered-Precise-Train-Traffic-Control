import random

def generate_train_data():
    stations = [
        "Chennai Central",
        "Madurai Junction",
        "Coimbatore Junction",
        "Trichy Junction",
        "Salem Junction"
    ]

    statuses = ["On Time", "Delayed", "Approaching", "Waiting"]

    trains = []

    for i in range(1, 8):
        scheduled = random.randint(100, 500)
        delay = random.randint(0, 25)

        train = {
            "train_id": f"T{i:03}",
            "train_name": f"Train-{i}",
            "current_station": random.choice(stations),
            "next_station": random.choice(stations),
            "scheduled_arrival": scheduled,
            "actual_arrival": scheduled + delay,
            "platform": random.randint(1, 3),
            "priority": random.randint(1, 5),  # 1 = highest priority
            "status": random.choice(statuses)
        }

        trains.append(train)

    return trains
