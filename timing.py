from openf1_client import get


def get_laps(session_key: int, driver_number: int | None = None):
    filters = [f"session_key={session_key}"]
    if driver_number:
        filters.append(f"driver_number={driver_number}")
    return get("laps", filters)
def get_stints(session_key: int, driver_number: int | None = None):
    filters = [f"session_key={session_key}"]
    if driver_number:
        filters.append(f"driver_number={driver_number}")
    return get("stints", filters)
def get_position(session_key: int, driver_number: int | None = None):
    filters = [f"session_key={session_key}"]
    if driver_number:
        filters.append(f"driver_number={driver_number}")
    return get("position", filters)
def get_intervals(session_key: int):
    return get("intervals", [f"session_key={session_key}"])
def get_car_data(session_key: int, driver_number: int, speed_filter: str | None = None):
    filters = [f"session_key={session_key}", f"driver_number={driver_number}"]
    if speed_filter:
        filters.append(speed_filter)   # e.g. "speed>=315"
    return get("car_data", filters)
def get_location(session_key: int, driver_number: int, date_from: str, date_to: str):
    filters = [
        f"session_key={session_key}",
        f"driver_number={driver_number}",
        f"date>{date_from}",
        f"date<{date_to}",
    ]
    return get("location", filters)
