import os
import uuid
import wave

from piper import PiperVoice

VOICE_MAP = {
    "en": "models/voices/en_US-lessac-medium.onnx",
    "hi": "models/voices/hi_IN-rohan-medium.onnx",
    "mr": "models/voices/hi_IN-rohan-medium.onnx"
}

_loaded_voices = {}

def get_voice(lang):

    model_path = VOICE_MAP.get(
        lang,
        VOICE_MAP["en"]
    )

    if model_path not in _loaded_voices:
        _loaded_voices[model_path] = PiperVoice.load(
            model_path
        )

    return _loaded_voices[model_path]


def generate_speech(text, lang="en"):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    output_file = f"outputs/{uuid.uuid4()}.wav"

    voice = get_voice(lang)

    with wave.open(output_file, "wb") as wav_file:
        voice.synthesize_wav(
            text,
            wav_file
        )

    return output_file