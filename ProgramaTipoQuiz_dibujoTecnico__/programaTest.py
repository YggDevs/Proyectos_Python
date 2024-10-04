import random
import tkinter as tk
from tkinter import messagebox

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

# Lógica de la aplicación
class TestApp:
    def __init__(self, root, preguntas, num_preguntas):
        self.root = root
        self.root.title("Test de Dibujo Técnico")
        self.preguntas = random.sample(preguntas, num_preguntas)
        self.respuestas_usuario = {}
        self.pregunta_actual = 0
        self.preguntas_falladas = []
        self.reintentando = False
        self.crear_widgets()

    def crear_widgets(self):
        self.pregunta_label = tk.Label(self.root, text="", wraplength=400)
        self.pregunta_label.pack(pady=10)

        self.opciones_var = tk.StringVar(value="")  # Ninguna opción seleccionada por defecto
        self.opciones_radio = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.opciones_var, value="")
            rb.pack(anchor="w")
            self.opciones_radio.append(rb)

        self.boton_siguiente = tk.Button(self.root, text="Siguiente", command=self.siguiente_pregunta)
        self.boton_siguiente.pack(pady=10)

        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        pregunta = self.preguntas[self.pregunta_actual]
        self.pregunta_label.config(text=pregunta["pregunta"])

        for i, opcion in enumerate(pregunta["opciones"]):
            self.opciones_radio[i].config(text=opcion, value=opcion)

        self.opciones_var.set("")  # Reiniciar la selección para cada pregunta

    def siguiente_pregunta(self):
        respuesta_seleccionada = self.opciones_var.get()
        if respuesta_seleccionada == "":
            messagebox.showwarning("Advertencia", "Por favor, selecciona una opción.")
            return

        pregunta = self.preguntas[self.pregunta_actual]
        correcta = respuesta_seleccionada == pregunta["respuesta_correcta"]
        self.respuestas_usuario[self.pregunta_actual] = correcta

        if not correcta and not self.reintentando:
            self.preguntas_falladas.append(pregunta)

        self.pregunta_actual += 1

        if self.pregunta_actual < len(self.preguntas):
            self.mostrar_pregunta()
        else:
            if self.reintentando:
                self.mostrar_resultados_finales()
            else:
                self.mostrar_resultados_falladas()

    def mostrar_resultados_falladas(self):
        if self.preguntas_falladas:
            messagebox.showinfo("Resultados", f"Has fallado {len(self.preguntas_falladas)} preguntas. Vamos a intentarlas de nuevo.")
            self.preguntas = self.preguntas_falladas
            self.preguntas_falladas = []
            self.pregunta_actual = 0
            self.reintentando = True
            self.mostrar_pregunta()
        else:
            self.mostrar_resultados_finales()

    def mostrar_resultados_finales(self):
        correctas = sum(self.respuestas_usuario.values())
        total = len(self.respuestas_usuario)
        messagebox.showinfo("Resultados", f"Has respondido correctamente {correctas} de {total} preguntas.")
        self.root.quit()

# Configuración inicial
if __name__ == "__main__":
    root = tk.Tk()
    preguntas = obtener_preguntas()
    app = TestApp(root, preguntas, num_preguntas=5)  # Puedes cambiar el número de preguntas aquí
    root.mainloop()


