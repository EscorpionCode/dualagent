# Chatbot Multi-Agente con Gemini y DeepSeek

Este proyecto implementa un chatbot en Python que utiliza dos modelos de lenguaje (LLMs) para generar y mejorar las respuestas:

1. **Generador:** Utiliza la API de Google Gemini para generar una respuesta inicial al mensaje del usuario.
2. **Evaluador/Optimizador:** Utiliza la API de Together.AI (con el modelo DeepSeek) para evaluar y mejorar la respuesta generada por Gemini.

Esta arquitectura multi-agente permite obtener respuestas más completas, precisas y refinadas que si se utilizara un solo modelo.

## Características

- **Arquitectura Multi-Agente:** Combina la potencia de dos LLMs (Gemini y DeepSeek) para generar respuestas de alta calidad.
- **Memoria de Conversación:** El chatbot recuerda los mensajes anteriores de la conversación, lo que permite mantener un diálogo coherente.
- **Interfaz de Terminal Mejorada:** Utiliza la librería `rich` para proporcionar una interfaz de usuario atractiva y fácil de usar en la terminal, con soporte para Markdown.
- **Limpieza de Memoria:** Incluye un comando (`limpiar`, `clear` o `reset`) para reiniciar la memoria de la conversación.
- **Solicitud Segura de Claves API:** Las claves API se solicitan al usuario de forma segura al inicio, en lugar de estar hardcodeadas en el código.
- **Manejo de Errores:** Incluye un manejo de errores básico para detectar problemas con las APIs.

## Requisitos

- Python 3.7+
- `requests`: Para realizar las llamadas a las APIs.

  ```bash
  pip install requests
  ```

- `rich`: Para la interfaz de terminal mejorada.

  ```bash
  pip install rich
  ```

- **Claves API:**
  - **Google Gemini:** Necesitas una clave API de Google para usar Gemini. Puedes obtenerla en [Google AI Studio](https://aistudio.google.com/).
  - **Together.AI:** Necesitas una clave API de Together.AI. Puedes obtenerla registrándote en [Together.AI](https://together.ai/). El modelo utilizado en este proyecto es `deepseek-ai/DeepSeek-R1`.

## Instalación

1. **Clona este repositorio:**

   ```bash
   git clone https://github.com/EscorpionCode/dualagent.git
   cd dualagent
   ```

2. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

   (Crea un archivo `requirements.txt` con el contenido `requests` y `rich` si no existe).

## Uso

1. **Ejecuta el script:**

   ```bash
   python chatbot.py
   ```

2. **Introduce tus claves API:** El script te pedirá tus claves API de Google Gemini y Together.AI. Introdúcelas cuando se te soliciten. Las claves se ocultan mientras las escribes.

3. **Interactúa con el chatbot:** Escribe tus mensajes en la terminal. El chatbot responderá utilizando la combinación de Gemini y DeepSeek.

4. **Comandos especiales:**

   - `salir` o `exit`: Para salir del chatbot.
   - `limpiar`, `clear` o `reset`: Para borrar la memoria de la conversación.

## Estructura del código

- `ChatMemory`: Clase para gestionar la memoria de la conversación.
- `call_generator_api()`: Función para llamar a la API de Gemini.
- `call_evaluator_api()`: Función para llamar a la API de Together.AI (DeepSeek).
- `chatbot()`: Función principal que gestiona la interacción con el usuario y la llamada a los agentes.
- Bloque `if __name__ == "__main__":`: Contiene el código principal que se ejecuta al iniciar el script. Solicita las claves API y llama a la función `chatbot()`.

## Notas Importantes

- **Costos:** El uso de las APIs de Google Gemini y Together.AI puede incurrir en costos. Consulta los precios de cada servicio antes de usar el chatbot de forma intensiva.
- **Modelos:** El código está configurado para usar `gemini-2.0-pro-exp-02-05` (Gemini) y `deepseek-ai/DeepSeek-R1` (Together.AI). Puedes cambiar estos modelos si tienes acceso a otros, pero es posible que tengas que ajustar el código para adaptarlo a la respuesta de la API. Asegúrate de que el modelo que elijas en Together.AI sea un modelo de chat (completions).
- **Manejo de Errores:** El manejo de errores actual es básico. En un entorno de producción, sería necesario implementar un manejo de errores más robusto (por ejemplo, reintentos, manejo de errores de red, validación de la respuesta de la API, etc.).
- **Seguridad de las claves API**: Nunca _commitees_ tus claves API a un repositorio público. Este script solicita las claves al usuario de forma segura, pero es importante que no las incluyas directamente en el código. Considera usar variables de entorno para una mayor seguridad.

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras algún error, tienes alguna sugerencia o quieres añadir nuevas funcionalidades, no dudes en abrir un _issue_ o enviar un _pull request_.
