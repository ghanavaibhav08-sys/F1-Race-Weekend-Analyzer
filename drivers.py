from openf1_client import get


def get_drivers(session_key: int):
    return get("drivers", [f"session_key={session_key}"])
def drivers_championship(session_key: int):
    return get("championship_drivers", [f"session_key={session_key}"])


def teams_championship(session_key: int):
    return get("championship_teams", [f"session_key={session_key}"])
