import cv2 as cv
 #valor 0 web cam ponemos valor 1 para camaras externas
capturavideo = cv.VideoCapture(1)      
if not capturavideo.isOpened():
    print("No se encontro una camara")
    exit()
while True:
    tipocamara,camara=capturavideo.read()
#pasar a grises las imagenes con cvtColor
    grises = cv.cvtColor(camara, cv.COLOR_BGR2GRAY)
    cv.imshow("Para salir presiona q ",camara)
  
    if cv.waitKey(1)==ord("q"):
        break
capturavideo.release()
cv.destroyAllWindows()