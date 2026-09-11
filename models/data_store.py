from collections import deque

latest_data = {
    "temp": 0,
    "hum": 0,
    "soil": 0,
    "light": 0,
    "pump": False,
    "time": ""
}

# store last 20 readings for chart
history = deque(maxlen=20)