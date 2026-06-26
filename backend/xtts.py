from TTS.api import TTS
from pydub import AudioSegment
import uuid
import os
import re

os.makedirs("outputs", exist_ok=True)

xtts = None


def get_xtts():

    global xtts

    if xtts is None:

        print("=" * 60)
        print("Loading XTTS Model...")
        print("=" * 60)

        xtts = TTS(
            model_name="tts_models/multilingual/multi-dataset/xtts_v2"
        )

        print("=" * 60)
        print("XTTS Ready")
        print("=" * 60)

    return xtts


SUPPORTED_LANGUAGES = {
    "en",
    "hi",
    "mr",
    "gu",
    "pa",
    "bn",
    "or",
    "kn",
    "ta",
    "te",
    "ml",
    "ur"
}


def clean_text(text):

    if not text:
        return ""

    text = (
        text.replace("AI", "A I")
            .replace("BAIF", "B A I F")
            .replace("ML", "M L")
            .replace("NLP", "N L P")
    )

    text = text.encode(
        "utf-8",
        errors="ignore"
    ).decode("utf-8")

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


def split_text(
    text,
    max_chars=100
):

    text = clean_text(text)

    separators = [
        "।",
        ".",
        "?",
        "!",
        "\n"
    ]

    sentences = [text]

    for sep in separators:

        temp = []

        for item in sentences:

            parts = item.split(sep)

            for p in parts:

                p = p.strip()

                if p:
                    temp.append(p)

        sentences = temp

    chunks = []

    current = ""

    for sentence in sentences:

        sentence = sentence.strip()

        # Split very large sentences
        if len(sentence) > max_chars:

            words = sentence.split()

            temp = ""

            for word in words:

                candidate_word = (
                    temp + " " + word
                ).strip()

                if len(candidate_word) > max_chars:

                    if temp:

                        chunks.append(
                            temp.strip()
                        )

                    temp = word

                else:

                    temp = candidate_word

            if temp:

                chunks.append(
                    temp.strip()
                )

            continue

        candidate = (
            current
            + " "
            + sentence
        ).strip()

        if len(candidate) > max_chars:

            if current:

                chunks.append(
                    current.strip()
                )

            current = sentence

        else:

            current = candidate

    if current:

        chunks.append(
            current.strip()
        )

    return chunks


def generate_xtts_speech(
    text,
    language,
    speaker_wav
):

    xtts_model = get_xtts()

    if language not in SUPPORTED_LANGUAGES:

        print(
            f"Unsupported language "
            f"{language}. "
            f"Using English."
        )

        language = "en"

    text = clean_text(text)

    chunks = split_text(
        text,
        max_chars=100
    )

    print("=" * 60)
    print(
        f"XTTS Chunks: "
        f"{len(chunks)}"
    )
    print("=" * 60)

    combined_audio = AudioSegment.empty()

    for idx, chunk in enumerate(chunks):

        print(
            f"Generating Chunk "
            f"{idx + 1}/"
            f"{len(chunks)}"
        )

        # Safety guard
        if len(chunk) > 240:

            print(
                f"Chunk too large "
                f"({len(chunk)} chars)"
            )

            chunk = chunk[:240]

        temp_file = (
            f"outputs/"
            f"{uuid.uuid4()}.wav"
        )

        xtts_model.tts_to_file(
            text=chunk,
            speaker_wav=speaker_wav,
            language=language,
            file_path=temp_file
        )

        chunk_audio = (
            AudioSegment.from_wav(
                temp_file
            )
        )

        combined_audio += chunk_audio

        # Natural pause between chunks
        combined_audio += (
            AudioSegment.silent(
                duration=800
            )
        )

        try:
            os.remove(
                temp_file
            )
        except:
            pass

    final_output = (
        f"outputs/"
        f"{uuid.uuid4()}.wav"
    )

    combined_audio.export(
        final_output,
        format="wav"
    )

    print("=" * 60)
    print(
        f"XTTS Success: "
        f"{final_output}"
    )
    print("=" * 60)

    return final_output