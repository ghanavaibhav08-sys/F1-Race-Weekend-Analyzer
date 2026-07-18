from openf1_client import get


def get_starting_grid(session_key: int):
    return get("starting_grid", [f"session_key={session_key}"])
def get_session_result(session_key: int):
    return get("session_result", [f"session_key={session_key}"])
