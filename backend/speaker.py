import ffmpeg
import os

def extract_speaker_reference(
    video_file,
    output_file="outputs/speaker_reference.wav"
):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    (
        ffmpeg
        .input(video_file, t=20)
        .output(
            output_file,
            ac=1,
            ar=22050
        )
        .overwrite_output()
        .run()
    )

    return output_file