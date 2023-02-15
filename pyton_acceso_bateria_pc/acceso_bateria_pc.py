#Para acceder a la información de la batería de un PC en Python, se puede utilizar la librería psutil. Primero, se debe instalar la librería con el siguiente comando en la terminal o línea de comandos:

#pip install psutil

#Luego, se puede usar el siguiente código para acceder a la información de la batería:


import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

print("Está conectado a la corriente: ", plugged)
print("Porcentaje de batería: ", percent)

#Este código imprimirá si el PC está conectado a la corriente y el porcentaje actual de la batería.