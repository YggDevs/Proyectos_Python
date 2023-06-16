from __future__ import print_function
import datetime
import os.path
import webbrowser
import tkinter as tk
from tkinter import messagebox
import time
import keyboard
import pyautogui as pg

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def enviarmensaje_instantaneamente(phone_no, message):
    webbrowser.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={message}")
    time.sleep(20)
    keyboard.press("enter")
    time.sleep(10)
    pg.hotkey("ctrl", "w")


def imprimir_proximos_eventos(events):
    """
    Función que imprime por consola la información de los próximos eventos, con la fecha y hora en un formato específico.

    Args:
        events (list): Lista de eventos.

    Returns:
        None
    """
    # Imprimir la información de cada evento
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        event_start = datetime.datetime.fromisoformat(start.replace('Z', '+00:00'))

        # Formatear la fecha y hora en el formato especificado
        formatted_start = event_start.strftime('%a %d %b %Y, %I:%M%p').replace('Mon', 'Lun').replace('Tue', 'Mar').replace(
            'Wed', 'Mié').replace('Thu', 'Jue').replace('Fri', 'Vie').replace('Sat', 'Sáb').replace('Sun', 'Dom').replace(
            'AM', 'AM').replace('PM', 'PM')

        print(f'Evento: {event["summary"]}')
        print(f'Fecha de inicio: {formatted_start}')


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next event on the user's calendar.
    """
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
                
                r'googleusercontent.com.json',                      #pega la ruta de tu archivo JSON de la api de GoogleCalendar
                
                SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            messagebox.showinfo('No upcoming events', 'No upcoming events found.')
            return

        # Print the next 10 events
        imprimir_proximos_eventos(events)

        # Get the start and name of the next event
        event = events[0]
        start = event['start'].get('dateTime', event['start'].get('date'))

        event_start = datetime.datetime.fromisoformat(start.replace('Z', '+00:00'))

        # formatear la fecha para que se muestre en un formato de  dia /mes/año
        formatted_start = event_start.strftime(
            '%a %d %b %Y, %I:%M%p').replace('Mon', 'Lun').replace('Tue', 'Mar').replace('Wed', 'Mié').replace(
            'Thu', 'Jue').replace('Fri', 'Vie').replace('Sat', 'Sáb').replace('Sun', 'Dom').replace('AM', 'AM').replace(
            'PM', 'PM')

        current_time = datetime.datetime.utcnow()
        if current_time.date() == event_start.date():
            messagebox.showinfo('Upcoming Event',
                                f'Proximo evento : {event["summary"]}\nHora de comienzo : {formatted_start}')

            #aqui deveras colocar el nombre del evento tal y como esta programado en tu google calendar seguido del numero de telefo de la persona que se le enviara un whatsapp
            contactos = {
                'Jhon Doe':'12345678',
                'Jhon Doe':'12345678',
                'Jhon Doe':'12345678',
                'Jhon Doe':'12345678',
                'Jhon Doe':'12345678',
                'Jhon Doe':'12345678',
                'Jhon Doe':'12345678',
                'Jhon Doe':'12345678',
                'Jhon Doe':'12345678',
                'Jhon Doe':'12345678',
                'Jhon Doe':'12345678'
                
            }

            nombre_contacto = event["summary"]  # Nombre del contacto obtenido del evento

            if nombre_contacto in contactos:
                numero_telefono = contactos[nombre_contacto]
                mensaje = f'Hola,te deseo un Feliz .\n{event["summary"]}\n  tu cumpleaños: {formatted_start}'
                enviarmensaje_instantaneamente(numero_telefono, mensaje)
            else:
                messagebox.showinfo('Contacto no encontrado', 'El contacto asociado al evento no se encuentra en la lista.')

        else:
            messagebox.showinfo('No upcoming events', 'No upcoming events found.')

    except HttpError as error:
        messagebox.showerror('API Error', f'An error occurred: {error}')


if __name__ == '__main__':
    main()