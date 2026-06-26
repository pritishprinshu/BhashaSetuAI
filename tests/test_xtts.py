from TTS.api import TTS

print("Loading XTTS...")

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2"
)

print("XTTS Loaded")

tts.tts_to_file(
    text="Welcome to Bhasha Setu A I.",
    speaker_wav="samples/speaker.wav",
    language="en",
    file_path="test.wav"
)

print("Audio Generated")