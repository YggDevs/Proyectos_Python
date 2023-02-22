import cv2
import pytesseract
"""
Este código utiliza la librería OpenCV para procesar una imagen de una matrícula de un vehículo, detectar el área donde se encuentra la matrícula, extraer esa región de la imagen y utilizar el módulo pytesseract para realizar reconocimiento óptico de caracteres (OCR) y obtener el texto contenido en la matrícula.

El proceso se realiza de la siguiente manera:

    Se carga la imagen utilizando la función cv2.imread() de OpenCV.
    Se convierte la imagen a escala de grises utilizando cv2.cvtColor().
    Se aplica un umbral para eliminar ruido y mejorar la detección de bordes utilizando cv2.GaussianBlur() y cv2.threshold().
    Se aplica la detección de bordes Canny utilizando cv2.Canny().
    Se encuentran los contornos en la imagen utilizando cv2.findContours().
    Se ordenan los contornos de mayor a menor área utilizando sorted().
    Se selecciona el contorno con el área más grande, que corresponde a la matrícula del vehículo.
    Se dibuja un rectángulo alrededor del contorno de la matrícula utilizando cv2.rectangle().
    Se extrae la región de la imagen dentro del rectángulo de la matrícula utilizando la variable de coordenadas x, y, w, h.
    Se configura el módulo pytesseract utilizando la variable pytesseract.pytesseract.tesseract_cmd, que especifica la ruta del ejecutable de Tesseract OCR en el sistema.
    Se aplica el OCR a la región de la matrícula utilizando pytesseract.image_to_string().
    Se muestra el texto extraído utilizando print().
    Se muestra la imagen resultante utilizando cv2.imshow().
    Se espera a que el usuario presione una tecla para cerrar la ventana utilizando cv2.waitKey().
    Se cierra la ventana si el usuario presiona la tecla 'q' utilizando cv2.destroyAllWindows().
"""



#instalar tesseract
# https://github.com/UB-Mannheim/tesseract/wiki

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

# Extraer la región de la imagen dentro del rectángulo de la matrícula
plate_roi = gray[y:y + h, x:x + w]

# Configurar el OCR
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

# Aplicar el OCR a la región de la matrícula
text = pytesseract.image_to_string(plate_roi, lang='spa')

# Mostrar el texto extraído
print("Matrícula: ", text)

# Mostrar la imagen resultante
cv2.imshow("Matrícula", img)
cv2.waitKey(0)

# Destruir la ventana al pulsar q
if(cv2.waitKey(1) & 0xFF == ord('q')):
    cv2.destroyAllWindows()
