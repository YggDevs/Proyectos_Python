import requests

url = "http://api.aviationstack.com/v1/flights"
"""
Aquí hay un ejemplo de cómo recuperar los vuelos diarios en un aeropuerto utilizando la API de aviationstack:

Recuerda reemplazar TU_API_KEY con tu propia clave de acceso de Aviationstack. También puedes modificar los parámetros de consulta según tus necesidades, 
como el número máximo de resultados que deseas mostrar o el estado de los vuelos que deseas recuperar.

"""

# Parámetros de consulta
params = {
    "access_key": "6bf0fead598862869b211af486d76e08",
    "airport_name": "BCN",  # Código IATA del aeropuerto de Barcelona
    "flight_status": "active",  # Mostrar solo vuelos activos
    "terminal": "1",
    "limit": 100  # Mostrar solo los 100 primeros resultados   
}

# Realiza la solicitud a la API
response = requests.get(url, params=params)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Recupera los datos de los vuelos
    flights = response.json()["data"]

    # Imprime los datos de los vuelos
    i=0    
    for flight in flights:
        print("Vuelo:", flight["flight"]["iata"])
        print("Compañía aérea:", flight["airline"]["name"])
        print("Hora de salida:", flight["departure"]["scheduled"])
        print("Hora de llegada:", flight["arrival"]["scheduled"])
        print("Estado del vuelo:", flight["flight_status"])
        print("-" * 100)
     
        i+=1
        print("numero de vuelos",{i})
else:
    print("Error al obtener los vuelos:", response.status_code)
