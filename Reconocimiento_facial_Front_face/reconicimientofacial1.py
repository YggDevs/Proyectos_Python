import cv2 as cv
#estamos capturando video de una camara exyerna por eso en VideoCaptura tenemos el parametro 1poner en 0 para webcam
camara=cv.VideoCapture(1)
""""Necesitas agregar cv2.data.haarcascadesantes de hacer referencia a la .xmlexpediente y concatenar 
da un error si solo especificamos el archivo xml podemos crear un path o si esta en el mismo directorio 
dejarlo como esta
"""
ruidos= cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_default.xml')

while True:
    _,captura=camara.read()
    #Convertimos la imagen a blanco y negro
    grises=cv.cvtColor(captura,cv.COLOR_BGR2GRAY)
    #Buscamos las coordenadas de los rostros 
    cara=ruidos.detectMultiScale(grises,1.3,5)
   #Dibujamos un rectángulo en las coordenadas de cada rostro
    numCaras = 1
    for (x,y,w,h) in cara:
        cv.rectangle(captura,(x,y),(x+w,y+h),(125,255,0),2)
        numCaras = numCaras + 1
    #Mostramos la imagen
    cv.imshow('img',captura)
    #Pulsando la tecla "q" salimos del programa
    if cv.waitKey(1) == ord('q'):
        break
 
print ("Se ha detectado el siguiente numero de caras: {}".format(numCaras))
