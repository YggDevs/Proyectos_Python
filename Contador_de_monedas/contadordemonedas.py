import numpy as np
import cv2

#variables 
valorGaus=1
valorkernel= 7

#ruta de los archivos
path="C:\Proyectos_Python\Contador_de_monedas\monedas.jpg"

# Cargamos la imagen y mostramos los resultados con imshow
original = cv2.imread(path)
cv2.imshow("original", original)       

# Convertimos a escala de grises
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
 
# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gris, (valorGaus,valorGaus), 0)
 
cv2.imshow("suavizado", gauss)          
# Detectamos los bordes con Canny
canny = cv2.Canny(gauss, 60, 100)
 
cv2.imshow("canny", canny)          

# Buscamos los contornos
#(contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

kernel = np.ones((valorkernel,valorkernel),np.uint8)
cierre=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
contornos , jerarquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


#dibujamos el color de los contornos
cv2.drawContours(original,contornos,-1,(0,0,255), 2)
cv2.imshow("contornos", original)
cv2.waitKey(0)


# Mostramos el número de monedas por consola

print("He encontrado {} objetos".format(len(contornos)))
