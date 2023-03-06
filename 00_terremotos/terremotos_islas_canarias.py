import requests
import folium

# Definir los parámetros de consulta
params = {
    'format': 'geojson',
    'starttime': '2020-01-01',
    'endtime': '2023-01-02',
    'minlatitude': 27,
    'maxlatitude': 29,
    'minlongitude': -18,
    'maxlongitude': -14,
    'minmagnitude': 2.5,
    'maxdepth': 100
}

# Hacer la petición GET a la API con los parámetros de consulta
response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query', params=params)

# Parsear la respuesta en formato JSON
json_data = response.json()

# Crear el objeto Folium Map centrado en las coordenadas de las islas canarias
mapa = folium.Map(location=[28, -16], zoom_start=8)

# Iterar sobre los terremotos registrados en el JSON
for terremoto in json_data['features']:
    # Obtener la información de interés
    fecha = terremoto['properties']['time']
    magnitud = terremoto['properties']['mag']
    profundidad = terremoto['geometry']['coordinates'][2]
    latitud = terremoto['geometry']['coordinates'][1]
    longitud = terremoto['geometry']['coordinates'][0]

    # Agregar un marcador al mapa
    folium.Marker(location=[latitud, longitud], popup=f'Magnitud: {magnitud} - Profundidad: {profundidad}').add_to(mapa)

# Guardar el mapa resultante en un archivo HTML
mapa.save('C:/Users/usuario/Desktop/proyectos_pitonIA/00_terremotos/terremotos.html')
print("Archivo creado ")

