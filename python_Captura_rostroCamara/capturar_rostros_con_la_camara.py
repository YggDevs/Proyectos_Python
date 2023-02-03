import cv2
import os

if not os.path.exists('C:/Proyectos_Python/python_rostro/Rostros_encontrados'):
    print('Carpeta creada en la ruta : C:/Proyectos_Python/python_rostro/Rostros_encontrados')
    os.makedirs('C:/Proyectos_Python/python_rostro/Rostros_encontrados')
camara = cv2.VideoCapture(0,cv2.CAP_DSHOW)

RostrosQuitandoRuidos = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
iterador = 0
while True:
    ret,frame = camara.read()
    frame = cv2.flip(frame,1)
    imagenPasada_a_Gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    copiaDeImagen = frame.copy()
    caras = RostrosQuitandoRuidos.detectMultiScale(imagenPasada_a_Gris, 1.3, 5)
    tecla = cv2.waitKey(1)
    #if tecla == 27:# pulsar Esc para salir
    if tecla == ord('q'):
        break
    for (x,y,w,h) in caras:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(128,0,255),2)
        rostro = copiaDeImagen[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
        if tecla == ord('s'):
            cv2.imwrite('C:/Proyectos_Python/python_rostro/Rostros_encontrados/rostro_{}.jpg'.format(iterador),rostro)
            cv2.imshow('rostro',rostro)
            iterador = iterador +1
    cv2.rectangle(frame,(10,5),(450,25),(255,255,255),-1)
    #org: Son las coordenadas de la esquina inferior izquierda de su texto. Se representa como una tupla de 2 valores (X, Y). X 
    #representa la distancia desde el borde izquierdo e Y representa la distancia desde el borde superior de la imagen. 
    cv2.putText(frame,'Presione s, para almacenar los rostros encontrados',(10,20), 2, 0.5,(0, 0, 0),1,cv2.LINE_AA)
    cv2.putText(frame,'Presione q, para salir',(10,50), 2, 0.5,(0, 0, 0),1,cv2.LINE_AA)
    cv2.imshow('frame',frame)

#cv2.waitKey() 0 congela la pantalla hasta que se haga algo 1 esperara 1 milisegundo y despues continuara
  #  if cv2.waitKey(1) & 0xFF == ord('q'):
  #      break

camara.release()
cv2.destroyAllWindows()