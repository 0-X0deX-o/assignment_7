from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC

cal = Calendar()
cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')

event = Event()
event.add('summary', 'Python meeting about calendaring')
event.add('dtstart', datetime(2022,12,8,12,0,0,tzinfo=UTC))
event.add('dtend', datetime(2022,12,8,12,30,0,tzinfo=UTC))
event.add('dtstamp', datetime.today())
event['uid'] = '20050115T101010/27346262376@mxm.dk'
event.add('priority', 5)

cal.add_component(event)

with open('example.ics', 'wb') as f:
    f.write(cal.to_ical())
    f.close()