# 🎙️ Whisper Audio Transcriptor

Este proyecto permite transcribir automáticamente archivos de audio en formato `.wav` utilizando el modelo [Whisper](https://github.com/openai/whisper) de OpenAI. Está diseñado para funcionar en CPU y guardar cada transcripción en un archivo `.txt` individual.

---

## ✅ Características

- Transcripción automática de archivos `.wav` desde una carpeta específica.
- Soporte para ejecución en CPU (sin necesidad de GPU).
- Guarda cada resultado en un archivo `.txt` independiente.
- Mensajes informativos durante el proceso.
- Compatible con Python 3.8+

---

## 🧰 Requisitos

Instala las dependencias ejecutando:

```bash
pip install git+https://github.com/openai/whisper.git
pip install torch
```

> Nota: Whisper detectará automáticamente si estás usando CPU y cambiará a FP32.

---

## 📂 Estructura del proyecto

```
Whisper-Audio/
├── audios/              # Carpeta con archivos .wav a transcribir
├── transcripciones/     # Carpeta donde se guardarán los .txt generados
├── TRANSCRIPTOR.py      # Script principal
└── README.md            # Este archivo
```

---

## 🚀 Cómo usar

1. Coloca tus archivos `.wav` dentro de la carpeta `audios/`.
2. Ejecuta el script con Python:

```bash
python TRANSCRIPTOR.py
```

3. Revisa las transcripciones generadas dentro de la carpeta `transcripciones/`.

---

## 📌 Ejemplo de salida

Si tienes un archivo llamado `mi_audio.wav`, el script creará:

```
transcripciones/mi_audio.txt
```

Con el texto completo extraído del audio.

---

## 📝 Resumen del ejemplo incluido

El audio de ejemplo incluido (`mi_audio.wav`) explica cómo obtener un **certificado digital español desde el extranjero** mediante un proceso de cuatro pasos, donde el solicitante solo debe realizar uno: la **verificación por video** con su documento de identidad.

---

## 📄 Licencia

Este proyecto se proporciona sin garantía, con fines educativos y demostrativos.
