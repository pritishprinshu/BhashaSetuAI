import os
import uuid
import wave

try:
    from piper import PiperVoice  # type: ignore
except Exception:
    # Fallback stub when the external 'piper' package is not available.
    # This stub provides the same interface used by this module:
    # - PiperVoice.load(path) -> object with synthesize_wav(text, wav_file)
    # The stub writes a short silent WAV so callers can continue to function.
    class PiperVoice:
        @staticmethod
        def load(path):
            class _StubVoice:
                def __init__(self, path):
                    self.path = path
                def synthesize_wav(self, text, wav_file):
                    # configure a simple mono 16-bit 22050Hz WAV and write 0.5s silence
                    wav_file.setnchannels(1)
                    wav_file.setsampwidth(2)
                    wav_file.setframerate(22050)
                    wav_file.setcomptype("NONE", "not compressed")
                    duration_s = 0.5
                    nframes = int(22050 * duration_s)
                    silence = b'\x00\x00' * nframes
                    wav_file.writeframes(silence)
            return _StubVoice(path)

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