import openai
import os
import time
from io import StringIO

try:
    import readline
except ImportError:
    try:
        import pyreadline as readline
    except ImportError:
        try:
            import pyreadline3 as readline 
        except ImportError:
            print("No se pudo cargar readline. Las flechas pueden no funcionar.")
            readline = None

try:
    readline.read_history_file("historial.txt")
except FileNotFoundError:
    pass

openai.api_key = "sk-tu_clave_api_acá" 

def main():
    start_time = time.time()  

    while True:
        try:
            try:
                consulta = input("Escribí tu pregunta ('salir' para terminar): ")
                if not consulta.strip():
                    print("Por favor escribí algo.")
                    continue
                if consulta.lower() == "salir":
                    break
            except Exception as e:
                print("Error al leer la consulta:", e)
                continue

            try:
                print(f"You: {consulta}")
            except Exception as e:
                print("Error al mostrar la consulta:", e)
                continue

            try:
                respuesta = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": consulta}],
                    temperature=0.7,
                    max_tokens=100
                )
                print("chatGPT:", respuesta.choices[0].message.content.strip())
            except Exception as e:
                print("Error al llamar a la API:", e)

        except KeyboardInterrupt:
            print("\nPrograma finalizado por el usuario.")
            break
        except Exception as error:
            print("Error inesperado:", error)

    try:
        readline.write_history_file("historial.txt")
    except Exception as e:
        print("No se pudo guardar el historial:", e)

    analizar_codigo(__file__, start_time)

def analizar_codigo(nombre_archivo, tiempo_inicio):
    from radon.metrics import mi_visit, h_visit
    from radon.raw import analyze
    from radon.complexity import cc_visit

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
    except Exception as e:
        print("Error al leer el archivo para análisis:", e)
        return

    print("\n Análisis de métricas con Radon:")

    raw_metrics = analyze(codigo)
    comment_ratio = raw_metrics.comment_lines / raw_metrics.code_lines if raw_metrics.code_lines > 0 else 0

    print(f"comment_ratio: {comment_ratio:.2f} ({comment_ratio * 100:.1f}%)")
    if comment_ratio < 0.33:
        print(" El código tiene pocos comentarios. Considerá agregar más explicaciones.")

    halstead = h_visit(codigo)
    if halstead:
        effort = halstead[0].effort
        time_required = halstead[0].time
        print(f" halstead_effort: {effort:.2f}")
        print(f" halstead_timerequired (segundos estimados): {time_required:.2f}")
    else:
        print("No se pudo calcular Halstead.")

    tiempo_total = time.time() - tiempo_inicio
    print(f" Tiempo real de ejecución del programa: {tiempo_total:.2f} segundos")

if __name__ == "__main__":
    main()

import openai
import time

try:
    import readline
except ImportError:
    try:
        import pyreadline as readline
    except ImportError:
        try:
            import pyreadline3 as readline 
        except ImportError:
            print("No se pudo cargar readline. Las flechas pueden no funcionar.")
            readline = None

def leer_historial():
    try:
        readline.read_history_file("historial.txt")
    except FileNotFoundError:
        pass

def main():
    start_time = time.time() 

    while True:
        consulta_usuario = obtener_consulta()
        if consulta_usuario.lower() == "salir":
            break
        
        mostrar_consulta(consulta_usuario)
        respuesta_chatgpt = obtener_respuesta_chatgpt(consulta_usuario)
        mostrar_respuesta(respuesta_chatgpt)
    
    try:
        readline.write_history_file("historial.txt")
    except Exception as e:
        print("No se pudo guardar el historial:", e)

    analizar_codigo(__file__, start_time)
    
def obtener_consulta():
    while True:
        try:
            consulta = input("Escribí tu pregunta ('salir' para terminar): ")
            if not consulta.strip():
                print("Por favor escribí algo.")
                continue
            return consulta
        except Exception as e:
            print("Error al leer la consulta:", e)
            continue

def mostrar_consulta(consulta):
    print(f"You: {consulta}")

def obtener_respuesta_chatgpt(consulta):
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": consulta}],
            temperature=0.7,
            max_tokens=100
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        print("Error al llamar a la API:", e)
        return None

def mostrar_respuesta(respuesta):
    if respuesta:
        print("chatGPT:", respuesta)
    else:
        print("No se pudo obtener una respuesta.")

def analizar_codigo(nombre_archivo, tiempo_inicio):
    from radon.raw import analyze
    from radon.complexity import cc_visit, h_visit

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
    except Exception as e:
        print("Error al leer el archivo para análisis:", e)
        return

    print("\n Análisis de métricas con Radon:")

    raw_metrics = analyze(codigo)
    comment_ratio = raw_metrics.comment_lines / raw_metrics.code_lines if raw_metrics.code_lines > 0 else 0

    print(f" comment_ratio: {comment_ratio:.2f} ({comment_ratio * 100:.1f}%)")
    if comment_ratio < 0.33:
        print(" El código tiene pocos comentarios. Considerá agregar más explicaciones.")

    halstead = h_visit(codigo)
    if halstead:
        effort = halstead[0].effort
        time_required = halstead[0].time
        print(f" halstead_effort: {effort:.2f}")
        print(f" halstead_timerequired (segundos estimados): {time_required:.2f}")
    else:
        print("No se pudo calcular Halstead.")

    tiempo_total = time.time() - tiempo_inicio
    print(f" Tiempo real de ejecución del programa: {tiempo_total:.2f} segundos")

if __name__ == "__main__":
    main()
    
import openai
import time

try:
    import readline
except ImportError:
    try:
        import pyreadline as readline
    except ImportError:
        try:
            import pyreadline3 as readline 
        except ImportError:
            print("No se pudo cargar readline. Las flechas pueden no funcionar.")
            readline = None

def leer_historial():
    try:
        readline.read_history_file("historial.txt")
    except FileNotFoundError:
        pass

def main():
    start_time = time.time() 

    while True:
        consulta_usuario = obtener_consulta()
        if consulta_usuario.lower() == "salir":
            break
        
        mostrar_consulta(consulta_usuario)
        respuesta_chatgpt = obtener_respuesta_chatgpt(consulta_usuario)
        mostrar_respuesta(respuesta_chatgpt)
    
    try:
        readline.write_history_file("historial.txt")
    except Exception as e:
        print("No se pudo guardar el historial:", e)

    analizar_codigo(__file__, start_time)
    sugerir_mejoras()

def obtener_consulta():
    while True:
        try:
            consulta = input("Escribí tu pregunta ('salir' para terminar): ")
            if not consulta.strip():
                print("Por favor escribí algo.")
                continue
            return consulta
        except Exception as e:
            print("Error al leer la consulta:", e)
            continue

def mostrar_consulta(consulta):
    print(f"You: {consulta}")

def obtener_respuesta_chatgpt(consulta):
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": consulta}],
            temperature=0.7,
            max_tokens=100
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        print("Error al llamar a la API:", e)
        return None

def mostrar_respuesta(respuesta):
    if respuesta:
        print("chatGPT:", respuesta)
    else:
        print("No se pudo obtener una respuesta.")

def analizar_codigo(nombre_archivo, tiempo_inicio):
    from radon.raw import analyze
    from radon.complexity import cc_visit, h_visit

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
    except Exception as e:
        print("Error al leer el archivo para análisis:", e)
        return

    print("\n Análisis de métricas con Radon:")

    raw_metrics = analyze(codigo)
    comment_ratio = raw_metrics.comment_lines / raw_metrics.code_lines if raw_metrics.code_lines > 0 else 0

    print(f"comment_ratio: {comment_ratio:.2f} ({comment_ratio * 100:.1f}%)")
    if comment_ratio < 0.33:
        print(" El código tiene pocos comentarios. Considerá agregar más explicaciones.")

    halstead = h_visit(codigo)
    if halstead:
        effort = halstead[0].effort
        time_required = halstead[0].time
        print(f" halstead_effort: {effort:.2f}")
        print(f" halstead_timerequired (segundos estimados): {time_required:.2f}")
    else:
        print("No se pudo calcular Halstead.")

    tiempo_total = time.time() - tiempo_inicio
    print(f"Tiempo real de ejecución del programa: {tiempo_total:.2f} segundos")
    
def sugerir_mejoras():
    consulta = "Por favor, sugiéreme posibles mejoras para este código Python que interactúa con la API de OpenAI, incluyendo sugerencias sobre eficiencia, legibilidad, y mejores prácticas."
    
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": consulta}],
            temperature=0.7,
            max_tokens=200
        )
        print("\n💡 Sugerencias de ChatGPT para mejorar el código:")
        print(respuesta.choices[0].message.content.strip())
    except Exception as e:
        print("Error al llamar a la API para sugerencias:", e)

if __name__ == "__main__":
    main()
   