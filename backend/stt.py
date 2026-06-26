from faster_whisper import WhisperModel

# Demo = "small"
# Production = "large-v3"
MODEL_SIZE = "large-v3"

model = None


def get_whisper():

    global model

    if model is None:

        print("=" * 60)
        print("Loading Whisper Model...")
        print(f"Model: {MODEL_SIZE}")
        print("=" * 60)

        model = WhisperModel(
            MODEL_SIZE,
            device="cpu",
            compute_type="int8"
        )

        print("=" * 60)
        print("Whisper Ready")
        print("=" * 60)

    return model


LANG_MAP = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Odia": "or",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Urdu": "ur"
}


def transcribe_audio(
    audio_path,
    source_lang_ui="Auto Detect"
):

    print("=" * 60)
    print("STARTING WHISPER AUDIO")
    print(audio_path)
    print("=" * 60)

    model = get_whisper()

    language = None

    if source_lang_ui != "Auto Detect":

        language = LANG_MAP.get(
            source_lang_ui
        )

    segments, info = model.transcribe(
    audio_path,
    language=language,
    beam_size=5,
    vad_filter=True,
    word_timestamps=True
)

    transcript = ""

    segment_count = 0

    for segment in segments:

        transcript += (
            segment.text + " "
        )

        segment_count += 1

    detected_language = (
        info.language
    )

    print("=" * 60)
    print(
        f"WHISPER AUDIO COMPLETE "
        f"({segment_count} segments)"
    )
    print(
        f"Language: {detected_language}"
    )
    print("=" * 60)

    return (
        transcript.strip(),
        detected_language
    )


def transcribe_segments(
    audio_path,
    source_lang_ui="Auto Detect"
):

    print("=" * 60)
    print("STARTING WHISPER SEGMENTS")
    print(audio_path)
    print("=" * 60)

    model = get_whisper()

    language = None

    if source_lang_ui != "Auto Detect":

        language = LANG_MAP.get(
            source_lang_ui
        )

    segments, info = model.transcribe(
        audio_path,
        language=language,
        beam_size=1,
        vad_filter=True,
        word_timestamps=True
    )

    result = []

    for segment in segments:

        text = segment.text.strip()

        if text:

            result.append(
                {
                    "start": segment.start,
                    "end": segment.end,
                    "text": text
                }
            )

    detected_language = (
        info.language
    )

    print("=" * 60)
    print(
        f"WHISPER COMPLETE: "
        f"{len(result)} segments"
    )
    print(
        f"Language: {detected_language}"
    )
    print("=" * 60)

    return (
        result,
        detected_language
    )