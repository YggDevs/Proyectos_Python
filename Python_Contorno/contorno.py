import cv2
# path ese necesario especificar un path si no da error
path = r'C:\Proyectos_Python\MonedasContorno\contorno.jpg'
# Reading an image in default mode
image = cv2.imread(path)

# pasamos a grises
Pasar_agris= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#contornos de imagenes
_,umbral = cv2.threshold(Pasar_agris,100,255,cv2.THRESH_BINARY )

#funcion para fijar los contornos

contornos,jerarquia=cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

# aqui se van a dibujar los contornos (imagen,contrornos,-1 es para que se fijen todos los contornos de la imagen,(poner colores RGB),3 es el grosor)
cv2.drawContours (image,contornos,-1,(251,60,50),3)
# Window name in which image is displayed
window_nameOR = 'imagen original'
window_nameGR = 'imagen pasada a grises'
window_nameUM = 'imagen con umbrales delimitados'

# Using cv2.imshow() method
# Display con imagen original
cv2.imshow(window_nameOR, image)

#Display con imagen en esvala de grises
cv2.imshow(window_nameGR, Pasar_agris)

#Display con imagen umbrales delimitados
cv2.imshow(window_nameUM,umbral)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()