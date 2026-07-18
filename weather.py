from openf1_client import get


def get_weather(meeting_key: int):
    return get("weather", [f"meeting_key={meeting_key}"])
