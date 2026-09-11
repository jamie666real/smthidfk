import os
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo


ALIASES = {
    "UTC": "UTC",
    "GMT": "GMT",
    "EST": "America/New_York",
    "EDT": "America/New_York",
    "CST": "America/Chicago",
    "CDT": "America/Chicago",
    "MST": "America/Denver",
    "MDT": "America/Denver",
    "PST": "America/Los_Angeles",
    "PDT": "America/Los_Angeles",
    "JST": "Asia/Tokyo",
    "AEST": "Australia/Sydney",
    "IST": "Asia/Kolkata",
    "CET": "Europe/Berlin",
    "EET": "Europe/Athens",
    "BST": "Europe/London",
    "SGT": "Asia/Singapore",
    "HKT": "Asia/Hong_Kong",
    "BRT": "America/Sao_Paulo",
}


def get_timezone():
    while True:
        tz_input = input(
            "Enter a timezone (examples: CST, America/New_York, UTC): "
        ).strip()

        if not tz_input:
            print("Timezone cannot be empty. Please try again.")
            continue

        try:
            return ZoneInfo(tz_input)
        except Exception:
            alias = ALIASES.get(tz_input.upper())
            if alias:
                return ZoneInfo(alias)

            print(
                "That timezone is not recognized. "
                "Try a common zone like CST, UTC, or America/New_York."
            )


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    tz = get_timezone()
    print(f"Current time in {tz}:")

    try:
        while True:
            now = datetime.now(tz)
            print(
                now.strftime("%Y-%m-%d %H:%M:%S %Z"),
                end="\r",
            )
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")
        sys.exit(0)


if __name__ == "__main__":
    main()
