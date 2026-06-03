from faster_whisper import WhisperModel

model = WhisperModel(
    "medium",
    device="auto",
    compute_type="int8"
)

LANGUAGE_MAP = {
    "hi": "Hindi",
    "mr": "Marathi",
    "en": "English"
}


def transcribe_audio(audio_path, source_lang="Auto Detect"):

    if source_lang == "Marathi":
        language = "mr"

    elif source_lang == "Hindi":
        language = "hi"

    elif source_lang == "English":
        language = "en"

    else:
        language = None

    segments, info = model.transcribe(
        audio_path,
        task="transcribe",
        language=language,
        beam_size=5,
        vad_filter=True,
        vad_parameters=dict(
            min_silence_duration_ms=500
        )
    )

    transcript = " ".join(
        segment.text.strip()
        for segment in segments
    )

    detected_language = LANGUAGE_MAP.get(
        info.language,
        "English"
    )

    return transcript.strip(), detected_language