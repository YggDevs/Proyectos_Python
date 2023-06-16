import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def obtener_eventos():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                
                r'googleusercontent.com.json',      #paste path of your route for yor JSON archive
                
                SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Set the start and end dates for events retrieval
        start_date = datetime.datetime(2023, 1, 1)
        end_date = datetime.datetime(2023, 12, 1)
        now = start_date.isoformat() + 'Z'  # 'Z' indicates UTC time
        end = end_date.isoformat() + 'Z'

        # Call the Calendar API with timeMin and timeMax parameters
        events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=end,
                                              singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        return events

    except HttpError as error:
        print(f'An error occurred: {error}')
        return []


# Ejemplo de uso:
eventos = obtener_eventos()
for event in eventos:
    print(f'Evento: {event["summary"]}')
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(f'Fecha de inicio: {start}')
    print('---')
