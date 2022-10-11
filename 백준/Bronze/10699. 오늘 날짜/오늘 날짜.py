from datetime import datetime, timedelta, timezone

print(datetime.today().astimezone(timezone(timedelta(hours=9))).strftime('%Y-%m-%d'))