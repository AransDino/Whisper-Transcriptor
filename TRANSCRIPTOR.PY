import os
import whisper
import warnings

# Silenciar advertencias innecesarias (como FP16 en CPU)
warnings.filterwarnings("ignore", category=UserWarning)

# Ruta de la carpeta con los audios
carpeta_audios = "./audios"

# Verificar que la carpeta exista
if not os.path.exists(carpeta_audios):
    print(f"❌ La carpeta '{carpeta_audios}' no existe. Crea la carpeta o cambia la ruta en el script.")
    exit()

# Cargar el modelo Whisper
print("🔄 Cargando modelo Whisper (base)...")
model = whisper.load_model("base")  # Puedes usar 'small', 'medium', 'large' si tienes GPU

# Crear carpeta de salida si no existe
carpeta_salida = "./transcripciones"
os.makedirs(carpeta_salida, exist_ok=True)

# Recorrer todos los archivos .wav en la carpeta
for nombre_archivo in os.listdir(carpeta_audios):
    if nombre_archivo.lower().endswith(".wav"):
        ruta_audio = os.path.join(carpeta_audios, nombre_archivo)
        nombre_sin_extension = os.path.splitext(nombre_archivo)[0]
        ruta_salida = os.path.join(carpeta_salida, f"{nombre_sin_extension}.txt")

        print(f"\n🎙️ Transcribiendo: {nombre_archivo}")
        try:
            resultado = model.transcribe(ruta_audio)
            texto = resultado["text"].strip()

            with open(ruta_salida, "w", encoding="utf-8") as archivo:
                archivo.write(texto)

            print(f"✅ Transcripción guardada en: {ruta_salida}")
        except Exception as e:
            print(f"❌ Error con {nombre_archivo}: {e}")

print("\n🎉 Todas las transcripciones han finalizado.")
