from openf1_client import get


def find_meeting(year: int, country_name: str):
    meetings = get("meetings", [f"year={year}", f"country_name={country_name}"])
    return meetings[0] if meetings else None
def list_sessions(meeting_key: int):
    return get("sessions", [f"meeting_key={meeting_key}"])


def find_session(meeting_key: int, session_name: str):
    sessions = get(
        "sessions",
        [f"meeting_key={meeting_key}", f"session_name={session_name}"],
    )
    return sessions[0] if sessions else None
