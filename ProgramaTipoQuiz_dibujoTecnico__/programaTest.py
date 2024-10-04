# Función que devuelve las preguntas y las opciones
def obtener_preguntas():
    preguntas = [
        {
            "pregunta": "¿Cuál de las siguientes normas regula el formato del papel para dibujo técnico?",
            "opciones": ["a) ISO 3098", "b) UNE 1026", "c) ISO 128", "d) UNE 1034"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Qué tipo de dibujo se realiza sin la ayuda de instrumentos y respeta en la medida de lo posible las proporciones?",
            "opciones": ["a) Plano", "b) Esquema", "c) Croquis", "d) Acotación"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Qué característica NO es propia de un croquis?",
            "opciones": ["a) Se realiza a mano alzada", "b) No sigue estrictamente una escala", "c) Utiliza colores para resaltar detalles", "d) Se acotan las medidas posteriormente"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Cuál es el primer paso antes de realizar un croquis?",
            "opciones": ["a) Acotar las dimensiones", "b) Seleccionar las vistas necesarias", "c) Analizar la pieza", "d) Replantear el dibujo sobre el papel"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Qué tipo de escala indica que el tamaño del dibujo es mayor al del objeto real?",
            "opciones": ["a) Escala natural", "b) Escala de ampliación", "c) Escala de reducción", "d) Escala 1:1"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Cuál es la fórmula correcta para calcular una escala?",
            "opciones": ["a) Escala = Tamaño del objeto real / Tamaño del dibujo", 
                         "b) Escala = Tamaño del dibujo / Tamaño real", 
                         "c) Escala = Tamaño del objeto real x Tamaño del dibujo", 
                         "d) Escala = Tamaño real + Tamaño del dibujo"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Qué tipo de esquema utiliza una sola línea para representar cada circuito, independientemente del número de conductores?",
            "opciones": ["a) Esquema multifilar", "b) Esquema unifilar", "c) Esquema de bloques", "d) Esquema de detalle"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿En qué tipo de esquema se representan todas las líneas de cada circuito y se identifican cada uno de los conductores?",
            "opciones": ["a) Esquema multifilar", "b) Esquema unifilar", "c) Esquema de principio", "d) Esquema de bloques"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "¿Qué símbolo se utiliza para representar el diámetro en un proceso de acotación?",
            "opciones": ["a) □", "b) R", "c) Φ", "d) SR"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Cuál de las siguientes afirmaciones es verdadera sobre las líneas de cota?",
            "opciones": ["a) Pueden cortarse con las líneas del dibujo", 
                         "b) Deben estar dibujadas en prolongación de las aristas de las piezas", 
                         "c) Deben estar a una distancia mínima de 8 mm del dibujo", 
                         "d) Se pueden dibujar en líneas ocultas"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Cuál es la función principal de las líneas auxiliares en un croquis?",
            "opciones": ["a) Delimitar los objetos dibujados", "b) Indicar cotas de las medidas", "c) Servir como guía para trazar líneas principales", "d) Definir el eje central de simetría"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Qué tipo de línea se utiliza en los dibujos técnicos para representar un objeto oculto?",
            "opciones": ["a) Línea continua gruesa", "b) Línea discontinua fina", "c) Línea de trazo y punto", "d) Línea continua delgada"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Qué símbolo se usa para indicar el radio en un proceso de acotación?",
            "opciones": ["a) □", "b) Φ", "c) R", "d) SR"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "Según la norma ISO 128, ¿qué características debe tener una línea continua gruesa en un dibujo técnico?",
            "opciones": ["a) Representar los contornos visibles de un objeto", 
                         "b) Mostrar las partes ocultas de un objeto", 
                         "c) Indicar los ejes de simetría", 
                         "d) Representar las líneas de cota"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "¿Qué normativa regula el uso de la escritura en los planos técnicos para asegurar legibilidad y uniformidad?",
            "opciones": ["a) UNE 1026", "b) UNE 1039", "c) ISO 5457", "d) UNE 1034"],
            "respuesta_correcta": "d"
        },
        {
            "pregunta": "¿Cuál de los siguientes esquemas es ideal para la representación de conexiones eléctricas simples?",
            "opciones": ["a) Esquema multifilar", "b) Esquema de bloques", "c) Esquema unifilar", "d) Plano de detalle"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Qué tipo de plano es necesario para indicar la ubicación exacta de las luminarias, interruptores y tomas de corriente en un proyecto eléctrico?",
            "opciones": ["a) Plano de zonificación", "b) Plano de trazado", "c) Plano de planta de la instalación eléctrica", "d) Plano topográfico"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Qué tipo de plano se utiliza para indicar las características físicas del terreno en un proyecto de obra civil?",
            "opciones": ["a) Plano de situación general", "b) Plano de estructura", "c) Plano topográfico", "d) Plano de zonificación"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Qué información se incluye en un plano de cimentación en un proyecto de edificación?",
            "opciones": ["a) La ubicación de luminarias e interruptores", 
                         "b) El recorrido de las canalizaciones eléctricas", 
                         "c) Las bases de sustentación, como zapatas y pilares", 
                         "d) La ubicación de las vías de evacuación"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Cuál es la función principal de una línea de referencia en un proceso de acotación?",
            "opciones": ["a) Indicar el diámetro de una pieza", 
                         "b) Conectar una nota explicativa con el objeto", 
                         "c) Marcar el eje de simetría", 
                         "d) Señalar las dimensiones no funcionales"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Qué tipo de cota es imprescindible para el correcto funcionamiento de una pieza?",
            "opciones": ["a) Cota funcional", "b) Cota auxiliar", "c) Cota no funcional", "d) Cota de situación"],
            "respuesta_correcta": "a"
        }
    ]
    return preguntas

# Función para corregir las respuestas
def corregir_examen(respuestas_usuario, preguntas):
    puntuacion = 0
    respuestas_incorrectas = []

    for i in range(len(preguntas)):
        if respuestas_usuario[i].lower() == preguntas[i]["respuesta_correcta"]:
            puntuacion += 1
        else:
            respuestas_incorrectas.append(i)

    return puntuacion, respuestas_incorrectas

# Función para permitir al usuario volver a responder preguntas incorrectas
def repetir_incorrectas(preguntas, respuestas_incorrectas):
    nuevas_respuestas = []
    for i in respuestas_incorrectas:
        print(f"Pregunta {i + 1}: {preguntas[i]['pregunta']}")
        for opcion in preguntas[i]["opciones"]:
            print(opcion)
        respuesta = input("Escribe tu respuesta (a, b, c, o d): ")
        nuevas_respuestas.append(respuesta)
    return nuevas_respuestas

# Función principal para ejecutar el test
def realizar_test():
    preguntas = obtener_preguntas()
    respuestas_usuario = []

    print("Examen tipo test sobre técnicas de dibujo, croquizado, proporciones y escalas, tipos de esquemas y cotas.\n")

    for i, pregunta in enumerate(preguntas):
        print(f"Pregunta {i + 1}: {pregunta['pregunta']}")
        for opcion in pregunta["opciones"]:
            print(opcion)
        
        respuesta = input("Escribe tu respuesta (a, b, c, o d): ")
        respuestas_usuario.append(respuesta)

    puntuacion, respuestas_incorrectas = corregir_examen(respuestas_usuario, preguntas)
    print(f"\nPuntuación obtenida: {puntuacion}/{len(preguntas)}")

    if respuestas_incorrectas:
        print(f"\nHas fallado en {len(respuestas_incorrectas)} pregunta(s).")
        repetir = input("¿Quieres intentar responderlas nuevamente? (s/n): ")
        if repetir.lower() == 's':
            nuevas_respuestas = repetir_incorrectas(preguntas, respuestas_incorrectas)
            for idx, nueva_respuesta in enumerate(nuevas_respuestas):
                if nueva_respuesta.lower() == preguntas[respuestas_incorrectas[idx]]["respuesta_correcta"]:
                    puntuacion += 1

    print(f"\nPuntuación final: {puntuacion}/{len(preguntas)}")
    if puntuacion == len(preguntas):
        print("¡Felicidades! Has obtenido la puntuación máxima.")
    elif puntuacion >= 16:
        print("¡Buen trabajo! Aprobaste el test.")
    else:
        print("No alcanzaste la puntuación mínima. Inténtalo nuevamente.")

# Ejecutar el test
realizar_test()

