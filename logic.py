import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from get_time import get_time
from read_excel import get_row, get_times

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main(path, names, emails):
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat()
    
    for j in range(0,len(names)):

      row = get_row(path,names[j])
      dates, start_times, end_times = get_times(path, row)

      for i in range(0,len(dates)):

          start, end = get_time(dates[i],start_times[i],end_times[i])
      
          event = {
              'summary': 'Work',
              #'location': '800 Howard St., San Francisco, CA 94103',
              'description': 'Penneys',
              'start': {
                  'dateTime': start,
                  'timeZone': 'GMT+1',
              },
              'end': {
                  'dateTime': end,
                  'timeZone': 'GMT+1',
              },
              'reminders': {
                  'useDefault': False,
              },
              'attendees': [
                {'email': emails[j]},
            ],
          }

          #event = service.events().insert(calendarId='primary', body=event).execute()
          print('Event created: %s' % (event.get('htmlLink')))


  except HttpError as error:
    print(f"An error occurred: {error}")

