from openf1_client import get


def get_pit_stops(session_key: int):
    return get("pit", [f"session_key={session_key}"])
def get_overtakes(session_key: int):
    return get("overtakes", [f"session_key={session_key}"])
def get_race_control(session_key: int):
    return get("race_control", [f"session_key={session_key}"])
def get_team_radio(session_key: int, driver_number: int | None = None):
    filters = [f"session_key={session_key}"]
    if driver_number:
        filters.append(f"driver_number={driver_number}")
    return get("team_radio", filters)
