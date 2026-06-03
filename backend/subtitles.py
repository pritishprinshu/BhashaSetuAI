import os

def generate_srt(text):

    os.makedirs("outputs", exist_ok=True)

    filename = "outputs/subtitles.srt"

    with open(filename, "w", encoding="utf-8") as f:

        f.write("1\n")
        f.write("00:00:00,000 --> 00:00:30,000\n")
        f.write(text)

    return filename