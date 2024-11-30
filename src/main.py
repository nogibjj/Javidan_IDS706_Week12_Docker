from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route("/")
def main_page():
    # Current time in UTC-5 (Eastern Standard Time)
    now_utc = datetime.utcnow()
    now = now_utc - timedelta(hours=5)  # Adjust to UTC-5

    # Set the New Year date for January 1, 2025, at 00:00 AM UTC-5
    new_year = datetime(2025, 1, 1, 0, 0, 0)

    # Time difference
    countdown = new_year - now

    # Pass remaining time components to the template
    days = countdown.days
    hours, remainder = divmod(countdown.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return render_template(
        "index.html",
        title="Countdown to New Year 2025 (UTC-5)",
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
