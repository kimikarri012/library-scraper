import datetime
import re
from bs4 import BeautifulSoup
from ics import Calendar, Event
import requests

# We will replace this URL with your actual library later
URL = "https://example.com/events"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
cal = Calendar()

# Let's add a dummy event just so the calendar file is generated successfully the first time
e = Event()
e.name = "Test Event: Script is Working!"
e.begin = datetime.datetime.now()
e.duration = datetime.timedelta(hours=1)
cal.events.add(e)

with open("toddler_events.ics", "w") as f:
    f.writelines(cal.serialize_iter())
