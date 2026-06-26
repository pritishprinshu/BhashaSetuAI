import os
import subprocess


def merge_translated_audio(
    original_video,
    translated_audio,
    output_video="outputs/translated_video.mp4"
):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    subprocess.run(
        [
            "ffmpeg",
            "-i",
            original_video,
            "-i",
            translated_audio,
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-shortest",
            output_video,
            "-y"
        ]
    )

    return output_video