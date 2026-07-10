def predict_delay(train):
    delay = train["actual_arrival"] - train["scheduled_arrival"]

    if delay <= 5:
        return delay + 2
    elif delay <= 15:
        return delay + 5
    else:
        return delay + 8
