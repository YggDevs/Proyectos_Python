import random
import tkinter as tk
from tkinter import simpledialog, messagebox

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
        }
    ]
    return preguntas

class TestApp:
    def __init__(self, root):
        self.root = root
        self.preguntas = obtener_preguntas()
        self.preguntas_falladas = []
        self.preguntas_actuales = []
        self.respuestas_usuario = {}
        self.pregunta_actual = 0
        self.reintentando = False

        # Pedir al usuario el número de preguntas
        self.numero_preguntas = simpledialog.askinteger("Número de preguntas", "¿Cuántas preguntas deseas responder?", minvalue=1, maxvalue=len(self.preguntas))
        if self.numero_preguntas is None:
            self.root.quit()

        # Seleccionamos las preguntas aleatoriamente
        self.preguntas_actuales = random.sample(self.preguntas, self.numero_preguntas)

        # Creamos la interfaz gráfica
        self.label_pregunta = tk.Label(root, text="")
        self.label_pregunta.pack(pady=20)

        self.var_respuesta = tk.StringVar()
        self.opcion1 = tk.Radiobutton(root, text="", variable=self.var_respuesta, value="a")
        self.opcion1.pack(anchor=tk.W)

        self.opcion2 = tk.Radiobutton(root, text="", variable=self.var_respuesta, value="b")
        self.opcion2.pack(anchor=tk.W)

        self.opcion3 = tk.Radiobutton(root, text="", variable=self.var_respuesta, value="c")
        self.opcion3.pack(anchor=tk.W)

        self.opcion4 = tk.Radiobutton(root, text="", variable=self.var_respuesta, value="d")
        self.opcion4.pack(anchor=tk.W)

        self.boton_siguiente = tk.Button(root, text="Siguiente", command=self.comprobar_respuesta)
        self.boton_siguiente.pack(pady=20)

        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        # Cargar la pregunta actual
        pregunta = self.preguntas_actuales[self.pregunta_actual]
        self.label_pregunta.config(text=pregunta["pregunta"])
        self.opcion1.config(text=pregunta["opciones"][0])
        self.opcion2.config(text=pregunta["opciones"][1])
        self.opcion3.config(text=pregunta["opciones"][2])
        self.opcion4.config(text=pregunta["opciones"][3])
        self.var_respuesta.set(None)  # Limpiar la selección previa

    def comprobar_respuesta(self):
        pregunta = self.preguntas_actuales[self.pregunta_actual]
        respuesta_correcta = pregunta["respuesta_correcta"]
        respuesta_usuario = self.var_respuesta.get()

        # Verificamos si el usuario ha seleccionado una opción
        if not respuesta_usuario:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una respuesta.")
            return

        # Comprobación de la respuesta del usuario
        if respuesta_usuario == respuesta_correcta:
            self.respuestas_usuario[self.pregunta_actual] = True
            messagebox.showinfo("Correcto", "¡Respuesta correcta!")
        else:
            self.respuestas_usuario[self.pregunta_actual] = False
            self.preguntas_falladas.append(pregunta)
            messagebox.showinfo("Incorrecto", f"Respuesta incorrecta. La respuesta correcta era: {respuesta_correcta}")

        # Avanzar a la siguiente pregunta
        self.pregunta_actual += 1

        if self.pregunta_actual < len(self.preguntas_actuales):
            self.mostrar_pregunta()
        else:
            self.finalizar_test()

    def finalizar_test(self):
        # Al finalizar el test
        if self.preguntas_falladas:
            reintento = messagebox.askyesno("Reintentar", "Has fallado algunas preguntas. ¿Quieres intentar nuevamente las preguntas falladas?")
            if reintento:
                self.reintentar_preguntas()
            else:
                self.mostrar_resultados()
        else:
            self.mostrar_resultados()

    def reintentar_preguntas(self):
        # Reintento de las preguntas falladas
        self.preguntas_actuales = self.preguntas_falladas
        self.preguntas_falladas = []
        self.pregunta_actual = 0
        self.reintentando = True
        self.mostrar_pregunta()

    def mostrar_resultados(self):
        # Mostrar los resultados finales
        correctas = sum(self.respuestas_usuario.values())
        total = len(self.respuestas_usuario)
        messagebox.showinfo("Resultados", f"Has respondido correctamente {correctas} de {total} preguntas.")
        self.root.quit()

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Test de Dibujo Técnico")
app = TestApp(root)
root.mainloop()

