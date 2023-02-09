import cv2
import pytesseract #https://pypi.org/project/pytesseract/

# Configuración de tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Inicialización de la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray,(5,5))
    canny = cv2.Canny(gray,150,200)
    canny = cv2.dilate(canny,None,iterations=1)
    cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        area = cv2.contourArea(c)
        x,y,w,h = cv2.boundingRect(c)
        epsilon = 0.09*cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,epsilon,True)
        
        if len(approx) == 4 and area > 9000:
            aspect_ratio = float(w) / h
            if aspect_ratio > 4.9:
                placa = gray[y:y+h,x:x+w]
                text = pytesseract.image_to_string(placa, config='--psm 11')
                print("Matrícula detectada:", text)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
                cv2.putText(frame, text, (x-20, y-10), 1, 2.2, (0, 255, 0), 3)
    
    cv2.imshow("Video", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


