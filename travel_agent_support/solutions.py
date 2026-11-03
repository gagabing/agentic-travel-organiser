from datetime import date
from typing import Any, Mapping


def _parse_date(value: Any) -> date | None:
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None


def validate(state: Mapping[str, Any], max_trip_days: int = 7) -> dict[str, list[str]]:
    request = state["request"]
    problems = []

    if not request.get("destination"):
        problems.append("the destination is missing")

    start_value = request.get("start_date")
    end_value = request.get("end_date")
    if not start_value or not end_value:
        problems.append("the exact start and end dates are missing")
    else:
        start_date = _parse_date(start_value)
        end_date = _parse_date(end_value)
        if start_date is None or end_date is None:
            problems.append("the start and end dates must be valid")
        elif end_date < start_date:
            problems.append("the end date is before the start date")
        elif start_date < date.today():
            problems.append("the start date is in the past")
        elif (end_date - start_date).days + 1 > max_trip_days:
            problems.append(
                f"the trip is longer than {max_trip_days} days "
                f"(this planner supports at most {max_trip_days})"
            )

    if not request.get("interests"):
        problems.append("no interests were given")

    return {"problems": problems}


