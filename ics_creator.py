from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime

# Create Calendar
cal = Calendar()

# necessary properties
cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')

# Create an event
event = Event()
event.add('summary', 'Exam Two Meeting')
event.add('dtstart', datetime(2022,12,9,12,0,0))
event.add('dtend', datetime(2022,12,9,13,0,0))
event.add('dtstamp', datetime(2022,12,7,19,00,0))


organizer = vCalAddress('MAILTO:liddle@iastate.edu')
organizer.params['cn'] = vText('David Liddle')
organizer.params['role'] = vText('CHAIR')
event['organizer'] = organizer
event['location'] = vText('Ames, IA')
event['uid'] = '202201219T101010/27346262376@mxm.dk'
event.add('priority', 5)

attendee = vCalAddress('MAILTO:liddle@iastate.edu')
attendee.params['cn'] = vText('David Liddle')
attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
event.add('attendee', attendee, encode=0)

attendee = vCalAddress('MAILTO:davidliddle23@gmail.com')
attendee.params['cn'] = vText('STUDENT')
attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
event.add('attendee', attendee, encode=0)

cal.add_component(event)

with open('example.ics', 'wb') as f:
    f.write(cal.to_ical())
    f.close()