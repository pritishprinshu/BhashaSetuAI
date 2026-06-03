import os
import subprocess

def extract_audio(video_path):

    os.makedirs("outputs", exist_ok=True)

    output_audio = "outputs/extracted_audio.wav"

    subprocess.run([
        "ffmpeg",
        "-i",
        video_path,
        "-vn",
        "-acodec",
        "pcm_s16le",
        "-ar",
        "16000",
        "-ac",
        "1",
        output_audio,
        "-y"
    ])

    return output_audio