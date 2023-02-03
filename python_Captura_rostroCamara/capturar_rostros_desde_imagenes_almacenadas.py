import cv2
import os

rutaDeImagenes = "C:/Proyectos_Python/python_Captura_rostroCamara/Imagenes"
listaDeImagenes = os.listdir(rutaDeImagenes)

if not os.path.exists('C:/Proyectos_Python/python_Captura_rostroCamara/Rostros_encontrados'):
    print('Carpeta creada ')
    os.makedirs('C:/Proyectos_Python/python_Captura_rostroCamara/Rostros_encontrados')

extraerCaras = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

count = 0
for NombreDeImagen in listaDeImagenes:
    imagen = cv2.imread(rutaDeImagenes+'/'+NombreDeImagen)
    copiaImagen = imagen.copy()
    imagenPasadaaGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    caras = extraerCaras.detectMultiScale(imagenPasadaaGris, 1.1, 5)

    for (x,y,w,h) in caras:
        cv2.rectangle(imagen, (x,y),(x+w,y+h),(128,0,255),2)
    cv2.rectangle(imagen,(10,5),(450,25),(255,255,255),-1)
    cv2.putText(imagen,'Presione s, para alamacenar los rostros encontrados',(10,20), 2, 0.5,(128,0,255),1,cv2.LINE_AA)
    cv2.imshow('image',imagen)
    tecla = cv2.waitKey(0)
    if  tecla == ord('s'):
        for (x,y,w,h) in caras:
            rostro = copiaImagen[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite('C:/Proyectos_Python/python_Captura_rostroCamara/Rostros_encontrados/rostro_{}.jpg'.format(count),rostro)
            count = count +1
    elif tecla == 27: #pulsa Esc para salir
        break

cv2.destroyAllWindows()