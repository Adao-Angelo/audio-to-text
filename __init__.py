import speech_recognition as sr

def audio_para_texto(caminho_arquivo):
    recognizer = sr.Recognizer()

    
    with sr.AudioFile(caminho_arquivo) as source:
        audio = recognizer.record(source)
    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        return texto
    except sr.UnknownValueError:
        return "Não foi possível entender o áudio"
    except sr.RequestError as e:
        return f"Erro ao acessar o serviço de reconhecimento de voz: {e}"


caminho_arquivo = "audio.wav"


texto_transcrito = audio_para_texto(caminho_arquivo)
print("Texto transcrito:")
print(texto_transcrito)


# comandos importantes
# sudo apt install ffmpeg
# ffmpeg -i seu_arquivo_de_audio.mp3 seu_arquivo_de_audio.wav

