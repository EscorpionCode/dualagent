import requests
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt

# Clase para gestionar la memoria (sin cambios)
class ChatMemory:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_history(self):
        return self.history

    def clear_history(self):  # Método para limpiar la memoria
        self.history = []


# Función modificada para usar Gemini
def call_generator_api(prompt, api_key, model="gemini-2.0-pro-exp-02-05"):  # Modelo más estándar y disponible
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

    params = {'key': api_key}
    headers = {'Content-Type': 'application/json'}

    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, json=data, headers=headers, params=params)

    if response.status_code == 200:
        response_json = response.json()

        # Extraer la respuesta de Gemini
        try:
            return response_json['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, IndexError):
            return "Error: Formato de respuesta inesperado de Gemini"
    else:
        raise Exception(f"Error Gemini: {response.status_code}, {response.text}")

# Función para Evaluador (sin cambios)
def call_evaluator_api(prompt, api_key, model="deepseek-ai/DeepSeek-R1"): # Modelo Mistral disponible en together.ai
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

def chatbot(api_key_gemini, api_key_together):
    memory = ChatMemory()
    console = Console()

    console.print("[bold blue]Bienvenido al Chatbot[/bold blue]")

    while True:
        user_input = Prompt.ask(":smiley: [bold]Usuario[/bold]") # Rich Prompt
        if user_input.lower() in ["salir", "exit"]:
            console.print("[bold red]Chatbot: ¡Hasta luego![/bold red]")
            break
        elif user_input.lower() in ["limpiar", "clear", "reset"]:  # Comando para limpiar la memoria
            memory.clear_history()
            console.print("[bold yellow]Chatbot: Memoria reiniciada.[/bold yellow]")
            continue  # Vuelve al inicio del bucle

        memory.add_message("user", user_input)


        # Agent 1: Ahora usando Gemini
        prompt_generator = f"Genera una respuesta detallada para: {user_input}"
        initial_response = call_generator_api(prompt_generator, api_key_gemini)  # pasa la api key correcta

        # Agent 2: Evaluador (se mantiene igual)
        prompt_evaluator = f"Evalúa esta respuesta y implementa mejoras/optimizaciones: {initial_response}"
        improved_response = call_evaluator_api(prompt_evaluator, api_key_together)

        # Mostrar respuesta con Markdown
        markdown = Markdown(f"{improved_response}")
        console.print(":robot: [bold green]Chatbot:[/bold green]")
        console.print(markdown)
        memory.add_message("assistant", improved_response)



# ---  MAIN  ---
if __name__ == "__main__":
    # Configuración y ejecución.  Pide las claves si no se han puesto.
    console = Console()

    # Obtener API key de Google / Gemini
    google_api_key = "" 
    if not google_api_key:
        console.print("[red]Error: Debes proporcionar una API key de Google.[/red]")
        exit()

    # Obtener API key de Together.AI
    together_api_key = "" 
    if not together_api_key:
        console.print("[red]Error: Debes proporcionar una API key de Together.AI.[/red]")
        exit()
    chatbot(google_api_key, together_api_key)
