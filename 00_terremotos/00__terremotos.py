import requests
import folium
import schedule
import time

# Definir la URL de la API de sismos del USGS
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'

# Definir la función que actualiza el mapa y guarda los datos sismicos cada 24 horas
def update_map():
    # Hacer la petición GET a la API
    response = requests.get(url)

    # Parsear la respuesta en formato JSON
    json_data = response.json()

    # Crear el objeto Folium Map centrado en las coordenadas del mundo
    mapa = folium.Map(location=[0, 0], zoom_start=2)

    # Iterar sobre los terremotos registrados en el JSON
    for terremoto in json_data['features']:
        # Obtener las coordenadas del terremoto y su magnitud
        latitud = terremoto['geometry']['coordinates'][1]
        longitud = terremoto['geometry']['coordinates'][0]
        magnitud = terremoto['properties']['mag']

        # Agregar un marcador al mapa
        folium.CircleMarker(location=[latitud, longitud], radius=magnitud*2, color='red', fill=True).add_to(mapa)

    # Guardar el mapa resultante en un archivo HTML
    mapa.save('C:/Users/usuario/Desktop/proyectos_pitonIA/terremotos.html')
    print("archivo creado")

    # Guardar los datos sismicos en un archivo de texto
    with open('datos_sismicos.txt', 'w') as archivo:
        archivo.write(response.text)

# Programar la ejecución de la función cada 24 horas
schedule.every(24).hours.do(update_map)

# Ejecutar la función una vez al inicio del programa
update_map()

# Mantener el programa en ejecución para que se puedan ejecutar las tareas programadas
while True:
    schedule.run_pending()
    time.sleep(1)









"""
import requests
import folium

# Definir la URL de la API de USGS para terremotos en los últimos 30 días
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'

# Hacer la petición GET a la API
response = requests.get(url)

# Obtener los datos en formato JSON
json_data = response.json()

# Crear el objeto Folium Map centrado en las coordenadas del mundo
mapa = folium.Map(location=[0, 0], zoom_start=2)

# Iterar sobre los terremotos registrados en el JSON
for terremoto in json_data['features']:
    # Obtener las coordenadas del terremoto y su magnitud
    latitud = terremoto['geometry']['coordinates'][1]
    longitud = terremoto['geometry']['coordinates'][0]
    magnitud = terremoto['properties']['mag']

    # Dibujar un marcador en el mapa
    folium.CircleMarker(location=[latitud, longitud], radius=magnitud*2, color='red', fill=True).add_to(mapa)

# Mostrar el mapa resultante
mapa.save('C:/Users/usuario/Desktop/proyectos_pitonIA/terremotos.html')
print("archivo creado")
"""