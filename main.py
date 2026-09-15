import os
import json
from datetime import date

from garminconnect import Garmin

EMAIL = os.environ.get("GARMIN_EMAIL")
PASSWORD = os.environ.get("GARMIN_PASSWORD")


def main():
    if not EMAIL or not PASSWORD:
        raise RuntimeError("Missing GARMIN_EMAIL or GARMIN_PASSWORD environment variables.")

    client = Garmin(EMAIL, PASSWORD)
    client.login()

    today = date.today().isoformat()
    profile = client.get_user_profile()
    stats = client.get_stats(today)

    result = {
        "date": today,
        "full_name": client.get_full_name(),
        "steps": stats.get("totalSteps"),
        "resting_heart_rate": stats.get("restingHeartRate"),
        "profile": profile,
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
    