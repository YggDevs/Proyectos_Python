import cv2
import numpy as np
import winsound
import time

# Carga el modelo pre-entrenado de YOLO
net = cv2.dnn.readNet("C:/Users/usuario/Desktop/proyectos_pitonIA/00_detectar_objetos_personas_con_yolo5/yolov3.weights", "C:/Users/usuario/Desktop/proyectos_pitonIA/00_detectar_objetos_personas_con_yolo5/yolov3.cfg")

# Define los nombres de las capas de salida
layer_names = net.getLayerNames()
output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]

# Define los nombres de las clases según el archivo COCO.names
classes = []
with open("C:/Users/usuario/Desktop/proyectos_pitonIA/00_detectar_objetos_personas_con_yolo5/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Inicializa la captura de video
cap = cv2.VideoCapture('C:/Users/usuario/Desktop/proyectos_pitonIA/00_detectar_objetos_personas_con_yolo5/gente-6387.mp4')

# Inicializa el contador de personas
person_count = 0

while True:
    # Lee el frame actual
    _, frame = cap.read()
    height, width, _ = frame.shape

    # Construye el blob desde el frame
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    # Pasa el blob a través de la red
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Inicializa las cajas y las probabilidades
    boxes = []
    confidences = []
    class_ids = []

    # Recorre cada salida de la red
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Obtiene las coordenadas de la caja
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectángulo con las coordenadas (x, y)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Agrega las cajas, las probabilidades y las clases a las listas
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Aplica NMS (Supresión de solapamiento múltiple)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Dibuja las cajas en el frame
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = (0, 255, 0)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 5), font , 1, color, 2)
            # Muestra el número de personas detectadas en el frame
    # Muestra el número de personas detectadas en el frame
    num_people = len([class_id for class_id in class_ids if classes[class_id] == 'Persona'])
    # Muestra el número de personas detectadas en el frame y el porcentaje
    num_people = len([class_id for class_id in class_ids if classes[class_id] == 'Persona'])
    percentage = num_people / len(class_ids) * 100
    cv2.putText(frame, f"Personas: {num_people} ({percentage:.2f}%)", (10, 50), font, 2, (0, 0, 255), 2)
    cv2.putText(frame, f"Personas: {num_people}", (10, 50), font, 2, (0, 0, 255), 2)
    
    # Calcula el 5% del total de personas detectadas
    num_people = len([class_id for class_id in class_ids if classes[class_id] == 'Persona'])
    five_percent = int(num_people * 0.05)

    # Muestra el número de personas detectadas y el 5% de las personas
    text = f"Personas: {num_people}   5%: {five_percent}"
    cv2.putText(frame, text, (10, 80), font, 2, (0, 0, 255), 2)

    # Sonido de alarma si se detecta una persona cada 20
    if num_people % 20 == 0:
        frequency = 2500  # frecuencia en Hz
        duration = 1000  # duración en milisegundos
        winsound.Beep(frequency, duration)
        cv2.putText(frame, 'Aleatorio', (width//2-50, height//2), font, 4, (0, 0, 255), 4)
        # Muestra la palabra "Aleatorio" durante 2 segundos
        
        # Dibuja un rectángulo rojo alrededor de la persona en la imagen
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Muestra la imagen con el rectángulo rojo durante 2 segundos
        cv2.imshow('Detector de personas', frame)
        cv2.waitKey(2000)
        
        
        cv2.imshow('Detector de personas', frame)
        cv2.waitKey(2000)
        
    cv2.imshow('Detector de personas', frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    
# Liberar los recursos
cap.release()
cv2.destroyAllWindows()