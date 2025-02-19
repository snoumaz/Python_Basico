"""
Assitente de Voz
"""
import pyttsx3
import speech_recognition as sr
import datetime


def audio_a_texto():
    
    # Objeto para reconocer el audio
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as source: # Importar el dispositivo de entrada

        # Tiempo de espera hasta que se activa el micro
        r.pause_threshold = 0.8 # Implementación de delay, antes de iniciar

        # Mensaje para el usuario para que ya puede hablar
        print("¿Cual es tu consulta?")

        # Variable para guardar el audio
        audio = r.listen(source)     

        try:
            # Reconocer el audio usando Bing
            text = r.recognize_bing(audio, language="es")

            # Mostrar en pantalla
            print("Voz reconocida:", text)
            return text

        except sr.UnknownValueError:
            print("El micro no funciona")
            return "Error"
        
        except sr.RequestError:
            print("No puede crear el texto")
            return "Error"

        except Exception as e:
            print(f"Error no identificado: {e}")
            return "Error"

# Llamar a la función para convertir audio a texto
#audio_a_texto()
id1="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id2="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
def respuesta_maquina(text):

    # Iniciar el motor de pyttx3
    engine = pyttsx3.init()

    # Ajustes 
    rate = engine.getProperty("rate")
    engine.setProperty("rate",100)
    volumen = engine.getProperty("volume")
    engine.setProperty("volume",1)
    engine.setProperty("voice", id2)
    engine.say(text)

    engine.runAndWait()

#respuesta_maquina("HOLA!!!!!!! ¿COMO ESTAS ERIKKKK?")
# engine = pyttsx3.init()
# for voz in engine.getProperty("voices"):
#     print(voz)

def decir_dia_semana():
    # Obtener dia de actual
    dia_actual = datetime.date.today()
    # print(dia_actual)
    dia_semana = dia_actual.weekday()
    # print(dia_semana)

    # nombres de los dias
    dias_esp = ("lunes","martes","miércoles","jueves","viernes","sabado","domingo")
    dias_eng = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")

    respuesta_maquina(f"Hoy es {dias_eng[dia_semana]}")

#decir_dia_semana()

def decir_hora():
    # guardar la hora
    hora_actual = datetime.datetime.now()
    #print(hora_actual)
    hora = f"Ahora son las {hora_actual.hour} y {hora_actual.minute} minutos"
    respuesta_maquina(hora)

#decir_hora()

def saludo_inicia():

    hora_actual = datetime.datetime.now().hour
    #print(hora_actual)
    # Momento del dia
    if 6 < hora_actual< 12:
        momento = "Buen dia Pixa!"
    elif 14 < hora_actual < 20:
        momento = "Illo que ya e tarde!!"
    else:
        momento = "Compaeee vamo que ya es de Noxee!!"
    
    saludo = f"{momento}, soy La Jenny, tu inasitente perzonal"

    respuesta_maquina(saludo)
    respuesta_maquina("¿Que Carajote quieres?")


#saludo_inicia()
 # Funcion que ejecuta el resto de funciones
def funcion_principal():
    # Primero saludo 
    saludo_inicia()

    # Bucle infinito para que escuche lo que le vamos a pedir
    activo = True
    while activo:
        peticion = audio_a_texto().lower()
        print(peticion)
        if peticion == "":
            activo = False

funcion_principal()