"""
Alura Agente - Agente Inteligente de Ventas
Lee un archivo CSV con datos de ventas y responde preguntas en lenguaje
natural sobre su contenido, usando el modelo Command R+ de Cohere a través
de LangChain.
"""

import os
import pandas as pd
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage

# -----------------------------------------------------------------------
# 1. CONFIGURACIÓN
# -----------------------------------------------------------------------
# Pega aquí tu API key gratuita de Cohere (https://dashboard.cohere.com/api-keys)
# O mejor aún: configúrala como variable de entorno antes de correr el script:
#   export COHERE_API_KEY="tu_api_key_aqui"
os.environ.setdefault("COHERE_API_KEY", "TU_API_KEY_AQUI")

CSV_PATH = "sales_data.csv"
MODEL_NAME = "command-a-plus-05-2026"

# -----------------------------------------------------------------------
# 2. LECTURA Y PROCESAMIENTO DEL DOCUMENTO
# -----------------------------------------------------------------------
def cargar_documento(path: str) -> str:
    """Lee el CSV con pandas y lo convierte a texto para dárselo de
    contexto al modelo de lenguaje."""
    df = pd.read_csv(path)
    return df.to_string(index=False)

# -----------------------------------------------------------------------
# 3. AGENTE DE IA
# -----------------------------------------------------------------------
def construir_agente(contexto: str):
    llm = ChatCohere(model=MODEL_NAME, temperature=0)

    def preguntar(pregunta: str) -> str:
        system_prompt = f"""Eres un asesor de ventas amigable y cercano que
ayuda a analizar los datos de una tienda. Respondes basándote ÚNICAMENTE en
la siguiente tabla de ventas, sin inventar datos que no estén ahí.

Estilo de respuesta:
- Habla en español, de forma natural y conversacional, como si le
  explicaras a un colega, no como un reporte técnico.
- Ve directo a la respuesta, sin mostrar tu proceso de razonamiento ni
  listar todos los datos que revisaste.
- Puedes agregar un pequeño comentario u observación útil cuando aporte
  valor (por ejemplo, si un producto destaca mucho sobre los demás).
- Evita sonar robótico o repetir la pregunta antes de responder.
- Sé breve: 1 a 3 frases, salvo que la pregunta pida más detalle.

DATOS DE VENTAS:
{contexto}
"""
        mensajes = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=pregunta),
        ]
        respuesta = llm.invoke(mensajes)
        contenido = respuesta.content

        # El modelo puede devolver una lista de bloques (razonamiento + texto).
        # Nos quedamos solo con el texto final de la respuesta.
        if isinstance(contenido, list):
            partes_texto = [
                bloque.get("text", "")
                for bloque in contenido
                if isinstance(bloque, dict) and bloque.get("type") == "text"
            ]
            return "".join(partes_texto).strip()

        return contenido

    return preguntar

# -----------------------------------------------------------------------
# 4. EJECUCIÓN
# -----------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Alura Agente - Asistente de Ventas ===")
    print(f"Documento cargado: {CSV_PATH}")
    print("Escribe tu pregunta o 'salir' para terminar.\n")

    contexto = cargar_documento(CSV_PATH)
    preguntar = construir_agente(contexto)

    # Ejemplo automático al iniciar (útil para la captura de pantalla del deploy)
    ejemplo = "¿Cuál fue el producto con mayor total de ventas?"
    print(f"Pregunta de ejemplo: {ejemplo}")
    print("Respuesta:", preguntar(ejemplo), "\n")

    while True:
        pregunta = input("Tu pregunta: ")
        if pregunta.strip().lower() in ("salir", "exit", "quit"):
            print("¡Hasta luego!")
            break
        respuesta = preguntar(pregunta)
        print("Respuesta:", respuesta, "\n")
