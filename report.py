from discovery import find_meeting, find_session
from drivers import get_drivers, drivers_championship, teams_championship
from results import get_starting_grid, get_session_result
from timing import get_laps, get_stints, get_position, get_intervals
from events import get_pit_stops, get_overtakes, get_race_control, get_team_radio
from weather import get_weather


def build_race_report(year: int, country_name: str) -> dict:
    meeting = find_meeting(year, country_name)
    if not meeting:
        raise ValueError(f"No meeting found for {country_name} {year}")
    meeting_key = meeting["meeting_key"]

    race_session = find_session(meeting_key, "Race")
    if not race_session:
        raise ValueError("No race session found for this meeting")
    session_key = race_session["session_key"]

    report = {
        "meeting": meeting,
        "session": race_session,
        "drivers": get_drivers(session_key),
        "championship_drivers": drivers_championship(session_key),
        "championship_teams": teams_championship(session_key),
        "starting_grid": get_starting_grid(session_key) or "no grid data for this session",
        "session_result": get_session_result(session_key),
        "laps": get_laps(session_key),
        "stints": get_stints(session_key),
        "pit_stops": get_pit_stops(session_key),
        "overtakes": get_overtakes(session_key),
        "race_control": get_race_control(session_key),
        "team_radio": get_team_radio(session_key),
        "weather": get_weather(meeting_key),
    }
    return report
def build_driver_deep_dive(session_key: int, driver_number: int):
    return {
        "laps": get_laps(session_key, driver_number),
        "stints": get_stints(session_key, driver_number),
        "position": get_position(session_key, driver_number),
        "team_radio": get_team_radio(session_key, driver_number),
    }
import json

def save_report(report: dict, filename: str = "race_report.json"):
    with open(filename, "w") as f:
        json.dump(report, f, indent=2, default=str)
