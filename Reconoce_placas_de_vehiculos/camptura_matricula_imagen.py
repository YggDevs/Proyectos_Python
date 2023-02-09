import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread('C:/Users/usuario/Desktop/proyectos_pitonIA/matricula.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar un umbral para eliminar el ruido y mejorar la detección de bordes
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(blurred, 160, 255, cv2.THRESH_BINARY)

# Aplicar la detección de bordes Canny
edges = cv2.Canny(thresh, 50, 150)

# Encontrar contornos en la imagen
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Ordenar los contornos de mayor a menor área
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Seleccionar el contorno con el área más grande
plate_contour = contours[0]

# Dibujar un rectángulo alrededor del contorno de la matrícula
x, y, w, h = cv2.boundingRect(plate_contour)
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Mostrar la imagen resultante
cv2.imshow("Matrícula", img)
cv2.waitKey(0)
cv2.destroyAllWindows()