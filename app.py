import streamlit as st
import tempfile
import os
import time
from moviepy import VideoFileClip
import wave

def estimate_processing_time(
    file_path,
    extension
):

    try:

        if extension in ["mp4", "mov"]:

            clip = VideoFileClip(file_path)

            duration = clip.duration

        else:

            from pydub import AudioSegment
            audio = AudioSegment.from_file(file_path)
            duration = len(audio) / 1000.0  

        estimated = int(
            duration * 0.5
        )

        return (
            int(duration),
            estimated
        )

    except:

        return 0, 0
        

from backend.stt import (
    transcribe_audio,
    transcribe_segments
)

from backend.translator import (
    translate_text,
    translate_segment
)
from backend.tts import generate_speech
from backend.subtitles import generate_srt
from backend.video import extract_audio
from backend.video_translate import merge_translated_audio
from backend.xtts import generate_xtts_speech
from backend.speaker import extract_speaker_reference

from ui import (
    load_ui,
    hero,
    feature_cards,
    footer
)

st.set_page_config(
    page_title="BhashaSetu AI",
    page_icon="🌐",
    layout="wide"
)

load_ui()
hero()
feature_cards()

st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns([1, 2])

with left:

    source_lang_ui = st.selectbox(
        "🎤 Source Language",
        [
            "Auto Detect",
            "English",
            "Hindi",
            "Marathi",
            "Gujarati",
            "Punjabi",
            "Bengali",
            "Odia",
            "Kannada",
            "Tamil",
            "Telugu",
            "Malayalam",
            "Urdu"
        ]
    )

    target_lang = st.selectbox(
        "🌍 Target Language",
        [
            "English",
            "Hindi",
            "Marathi",
            "Gujarati",
            "Punjabi",
            "Bengali",
            "Odia",
            "Kannada",
            "Tamil",
            "Telugu",
            "Malayalam",
            "Urdu"
        ]
    )

    voice_engine = st.selectbox(
        "🔊 Voice Engine",
        [
            "Fast (Piper)",
            "Natural (XTTS)"
        ]
    )

    output_mode = st.radio(
        "🎬 Output Type",
        [
            "Audio Only",
            "Translated Video"
        ],
        index=1
    )

    live_mode = st.checkbox(
        "⚡ Live Translation Mode",
        value=True
    )

with right:

    uploaded_file = st.file_uploader(
        "📂 Upload Audio or Video",
        type=[
            "mp3",
            "wav",
            "m4a",
            "mp4",
            "mov"
        ]
    )

if uploaded_file:

    st.success(
        f"✅ Uploaded: {uploaded_file.name}"
    )

    process_clicked = st.button(
        "🚀 Translate Content",
        use_container_width=True
    )

    progress_bar = st.progress(0)

    status_box = st.empty()

    timer_box = st.empty()

    live_transcript = st.empty()

    live_translation = st.empty()

    if process_clicked:

        temp_path = None
        duration_sec = 0
        eta_sec = 0
        
        try:

            with tempfile.NamedTemporaryFile(
                delete=False
            ) as tmp:

                tmp.write(
                    uploaded_file.read()
                )

                temp_path = tmp.name

            extension = (
                uploaded_file.name
                .split(".")[-1]
                .lower()
            )

            with st.spinner(
                "📂 Preparing File..."
            ):
                
                duration_sec = 0
                eta_sec = 0

                if extension in [
                    "mp4",
                    "mov"
                ]:

                    audio_path = extract_audio(
                        temp_path
                    )
                    duration_sec, eta_sec = (
                        estimate_processing_time(
                            temp_path,
                            extension
                        )
                    )

                    st.info(
                        f"⏱ Video Length: "
                        f"{duration_sec//60}m "
                        f"{duration_sec%60}s\n\n"
                        f"🚀 Estimated Translation Time: "
                        f"{eta_sec//60}m "
                        f"{eta_sec%60}s"
                    )
                    estimated_time = max(
                        eta_sec,
                        60
                    )

                else:

                    audio_path = temp_path

                    duration_sec, eta_sec = (
                        estimate_processing_time(
                            temp_path,
                            extension
                        )
                    )

                    st.info(
                        f"⏱ Audio Length: "
                        f"{duration_sec//60}m "
                        f"{duration_sec%60}s\n\n"
                        f"🚀 Estimated Translation Time: "
                        f"{eta_sec//60}m "
                        f"{eta_sec%60}s"
                    )

                    estimated_time = max(
                        eta_sec,
                        60
                    )

            progress_bar.progress(10)

            lang_map = {
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

            if live_mode:

                    status_box.info(
                        "🎤 Stage 1/4: Speech Recognition"
                    )

                    segments, source_lang = (
                        transcribe_segments(
                            audio_path,
                            source_lang_ui
                        )
                    )

                    process_start = time.time()

                    whisper_to_ui = {
                        "en": "English",
                        "hi": "Hindi",
                        "mr": "Marathi",
                        "gu": "Gujarati",
                        "pa": "Punjabi",
                        "bn": "Bengali",
                        "or": "Odia",
                        "kn": "Kannada",
                        "ta": "Tamil",
                        "te": "Telugu",
                        "ml": "Malayalam",
                        "ur": "Urdu"
                    }

                    source_lang = whisper_to_ui.get(
                        source_lang,
                        source_lang
                    )

                    st.success(
                        f"Detected Language: {source_lang}"
                    )

                    m1, m2, m3, m4 = st.columns(4)

                    m1.metric(
                        "Source",
                        source_lang
                    )

                    m2.metric(
                        "Target",
                        target_lang
                    )

                    m3.metric(
                        "Duration",
                        f"{duration_sec//60}:{duration_sec%60:02d}"
                    )

                    m4.metric(
                        "ETA",
                        f"{eta_sec//60}:{eta_sec%60:02d}"
                    )

                    full_transcript = ""
                    full_translation = ""

                    total_segments = max(
                        len(segments),
                        1
                    )

                    preview_generated = False

                    chunk_size = 5

                    preview_generated = False

                    for i in range(
                        0,
                        len(segments),
                        chunk_size
                    ):

                        batch = segments[
                            i:i + chunk_size
                        ]

                        batch_text = " ".join(
                            seg["text"]
                            for seg in batch
                        )

                        print(
                            f"Processing Batch "
                            f"{i // chunk_size + 1}"
                        )
                        status_box.info(
                            "🌍 Stage 2/4: Translation"
                        )

                        translated_batch = (
                            translate_segment(
                                batch_text,
                                source_lang,
                                target_lang
                            )
                        )

                        completed = min(
                            i + chunk_size,
                            len(segments)
                        )

                        elapsed = (
                            time.time()
                            - process_start
                        )

                        progress_ratio = (
                            completed
                            / len(segments)
                        )

                        if progress_ratio > 0:

                            estimated_total = (
                                elapsed
                                / progress_ratio
                            )

                            remaining = max(
                                0,
                                estimated_total - elapsed
                            )

                        else:

                            remaining = 0

                        full_transcript += (
                            batch_text + " "
                        )

                        full_translation += (
                            translated_batch + " "
                        )

                        live_transcript.text_area(
                            "📝 Live Transcript",
                            full_transcript,
                            height=250
                        )

                        live_translation.text_area(
                            "🌐 Live Translation",
                            full_translation,
                            height=250
                        )

                        progress = int(
                            (
                                min(
                                    i + chunk_size,
                                    len(segments)
                                )
                                / len(segments)
                            ) * 60
                        )

                        progress_bar.progress(
                            min(progress, 60)
                        )

                        completed = min(
                            i + chunk_size,
                            len(segments)
                        )

                        mins = int(
                            remaining // 60
                        )

                        secs = int(
                            remaining % 60
                        )

                        status_box.info(
                            f"🌍 Stage 2/4: Translation\n\n"
                            f"Progress: "
                            f"{completed}/{len(segments)} Segments\n\n"
                            f"⏳ ETA: "
                            f"{mins:02d}:{secs:02d}"
                        )

                        if (
                            not preview_generated
                            and i >= 5
                        ):

                            try:

                                if voice_engine == "Natural (XTTS)":

                                    preview_audio = generate_xtts_speech(
                                        full_translation,
                                        language=lang_map[target_lang],
                                        speaker_wav="samples/speaker.wav"
                                    )
                                else:   

                                    preview_audio = generate_speech(
                                        full_translation,
                                        lang_map[target_lang]
                                    )

                                st.success(
                                    "🎬 Preview Ready"
                                )

                                st.audio(
                                    preview_audio
                                )

                                preview_generated = True

                            except Exception as e:

                                print(
                                    f"Preview Error: {e}"
                                )

                    transcript = (
                        full_transcript.strip()
                    )

                    translated_text = (
                        full_translation.strip()
                    )

            else:

                status_box.info(
                    "🎤 Converting Speech To Text..."
                )

                transcript, source_lang = (
                    transcribe_audio(
                        audio_path,
                        source_lang_ui
                    )
                )

                st.success(
                    f"Detected Language: {source_lang}"
                )

                status_box.info(
                    "🌍 Translating..."
                )

                translated_text = (
                    translate_text(
                        transcript,
                        source_lang,
                        target_lang
                    )
                )

            progress_bar.progress(60)

            translated_video = None

            status_box.info(
                "🔊 Stage 3/4: Voice Generation\n\n"
                "⏳ ETA: Calculating..."
            )

            progress_bar.progress(70)

            if voice_engine == "Fast (Piper)":

                audio_file = (
                    generate_speech(
                        translated_text,
                        lang_map[target_lang]
                    )
                )

            else:

                if extension in [
                    "mp4",
                    "mov"
                ]:

                    speaker_wav = (
                        extract_speaker_reference(
                            temp_path
                        )
                    )

                else:

                    speaker_wav = (
                        "samples/speaker.wav"
                    )

                audio_file = (
                    generate_xtts_speech(
                        translated_text,
                        language=lang_map[target_lang],
                        speaker_wav=speaker_wav
                    )
                )

            if (
                output_mode == "Translated Video"
                and extension in [
                    "mp4",
                    "mov"
                ]
            ):

                status_box.info(
                    "🎬 Stage 4/4: Video Rendering\n\n"
                    "⏳ ETA: ~10-20 sec"
                )

                progress_bar.progress(90)

                translated_video = (
                    merge_translated_audio(
                        temp_path,
                        audio_file
                    )
                )

            status_box.info(
                "📜 Creating Subtitles..."
            )

            srt_file = (
                generate_srt(
                    translated_text
                )
            )

            progress_bar.progress(100)

            status_box.success(
                "✅ Translation Completed"
            )
            
            timer_box.success(
                "✅ Processing Complete"
            )

            st.markdown("---")

            col1, col2 = st.columns(2)

            with col1:

                st.subheader(
                    "📝 Transcript"
                )

                st.text_area(
                    "",
                    transcript,
                    height=300
                )

            with col2:

                st.subheader(
                    "🌐 Translation"
                )

                st.text_area(
                    "",
                    translated_text,
                    height=300
                )

            st.markdown("---")

            st.subheader(
                "🔊 Translated Voice"
            )

            st.audio(
                audio_file
            )

            with open(
                audio_file,
                "rb"
            ) as audio:

                st.download_button(
                    "⬇ Download Audio",
                    data=audio,
                    file_name="translated_audio.wav",
                    use_container_width=True
                )

            if translated_video:

                st.markdown("---")

                st.subheader(
                    "🎬 Translated Video"
                )

                st.video(
                    translated_video
                )

                with open(
                    translated_video,
                    "rb"
                ) as video_file:

                    st.download_button(
                        "⬇ Download Translated Video",
                        data=video_file,
                        file_name="translated_video.mp4",
                        use_container_width=True
                    )

            with open(
                srt_file,
                "rb"
            ) as file:

                st.download_button(
                    "⬇ Download Subtitle File",
                    data=file,
                    file_name="subtitles.srt",
                    use_container_width=True
                )

        except Exception as e:

            st.error(
                f"❌ Error: {str(e)}"
            )

        finally:

            try:

                if (
                    temp_path
                    and os.path.exists(
                        temp_path
                    )
                ):

                    os.remove(
                        temp_path
                    )

            except:
                pass

footer()