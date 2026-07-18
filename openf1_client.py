# openf1_client.py
import requests

BASE_URL = "https://api.openf1.org/v1"


def get(endpoint: str, filters: list[str] | None = None, csv: bool = False):
    filters = filters or []
    if csv:
        filters.append("csv=true")

    url = f"{BASE_URL}/{endpoint}"
    if filters:
        url += "?" + "&".join(filters)

    response = requests.get(url, timeout=15)

    if response.status_code == 404:
        # OpenF1 uses 404 to mean "no matching rows", not a real error
        return [] if not csv else ""

    response.raise_for_status()
    return response.json() if not csv else response.text
