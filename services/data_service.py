from datetime import datetime

_latest = {
    "temp": None,
    "hum": None,
    "soil": None,
    "light": None,
    "pump": None,
    "time": None
}

_history = []

def update_data(data):
    global _latest, _history

    _latest.update({
        "temp": data.get("temp"),
        "hum": data.get("hum"),
        "soil": data.get("soil"),
        "light": data.get("light"),
        "pump": data.get("pump"),
        "time": datetime.now().strftime("%H:%M:%S")
    })

    # keep last 20 records for chart
    _history.append(_latest.copy())
    if len(_history) > 20:
        _history.pop(0)

def get_data():
    return _latest

def get_history():
    return _history