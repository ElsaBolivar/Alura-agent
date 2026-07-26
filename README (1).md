# Alura Agente – Asistente Inteligente de Ventas

Proyecto final del programa **Alura + Oracle ONE - AI FOR TECH**.
Agente de inteligencia artificial que responde preguntas en lenguaje natural
sobre un documento de ventas (CSV), usando LangChain y el modelo Gemini de
Google, con despliegue en Oracle Cloud Infrastructure (OCI).

## 📌 Descripción del proyecto

Muchas veces perdemos tiempo revisando hojas de cálculo para responder
preguntas simples como "¿cuál fue el producto más vendido?". Este proyecto
resuelve ese problema: un agente de IA lee un archivo CSV de ventas y
responde cualquier pregunta sobre esos datos en español, de forma directa.

## 🏗️ Arquitectura de la solución

```
Usuario → Terminal (input) → agent.py → LangChain → Cohere (LLM) → Respuesta
                                 ↑
                          sales_data.csv (pandas)
```

1. **Carga de datos**: `pandas` lee el archivo `sales_data.csv` y lo
   convierte en texto.
2. **Contexto**: ese texto se inyecta como contexto en un *system prompt*
   con instrucciones de tono conversacional y humano.
3. **Modelo de lenguaje**: `langchain-cohere` envía la pregunta del
   usuario junto con el contexto al modelo `command-a-plus-05-2026`.
4. **Respuesta**: el modelo responde solo con base en los datos del CSV,
   de forma breve y natural.

## 🛠️ Tecnologías utilizadas

- **Python** 3.10+
- **Pandas** – lectura y procesamiento del CSV
- **LangChain** – orquestación del agente
- **Cohere** (`command-a-plus-05-2026`) – modelo de lenguaje
- **Oracle Cloud Infrastructure (OCI Compute)** – despliegue

## ▶️ Instrucciones para ejecutar el proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/alura-agente.git
   cd alura-agente
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Consigue una API key gratuita (Trial key) en [Cohere Dashboard](https://dashboard.cohere.com/api-keys)
   y configúrala:
   ```bash
   export COHERE_API_KEY="tu_api_key_aqui"
   ```
4. Ejecuta el agente:
   ```bash
   python agent.py
   ```

## 💬 Ejemplos de preguntas y respuestas

**Pregunta:** ¿Cuál fue el producto con mayor total de ventas?
**Respuesta:** El producto con el mayor total de ventas fue los Tenis Casuales, con un total de $420.

**Pregunta:** ¿Cuántas unidades se vendieron en San José?
**Respuesta:** En San José se vendieron 113 unidades en total.

**Pregunta:** ¿Cuáles recomiendas que sean las siguientes compras?
**Respuesta:** Basado en lo que se está vendiendo mejor, sugeriría reponer la Camiseta Básica (la más vendida en unidades y total), las Sandalias (gran volumen y buen total) y los Tenis Running (el total más alto). También vale la pena considerar la Gorra, que se vende mucho y es barata, y accesorios de alto margen como el Reloj para impulsar la rentabilidad.

## ☁️ Despliegue en OCI

El agente fue desplegado y ejecutado en una instancia **OCI Compute (Always
Free – Ubuntu)**. Evidencia del despliegue:

- Captura de pantalla: `deploy_evidence.png` (agregar en el repositorio)
- IP pública / instancia: _agregar aquí_

## 👤 Autor

Proyecto desarrollado como parte del Challenge final de **Alura + Oracle ONE
- AI FOR TECH**.
