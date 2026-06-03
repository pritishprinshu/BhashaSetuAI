import streamlit as st
import tempfile
import os

from backend.stt import transcribe_audio
from backend.translator import translate_text
from backend.tts import generate_speech
from backend.subtitles import generate_srt
from backend.video import extract_audio

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
            "Hindi",
            "Marathi",
            "English"
        ]
    )

    target_lang = st.selectbox(
        "🌍 Target Language",
        [
            "English",
            "Hindi",
            "Marathi"
        ]
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

    st.success(f"✅ Uploaded: {uploaded_file.name}")

    process_clicked = st.button(
        "🚀 Translate Content",
        use_container_width=True
    )

    if process_clicked:

        try:

            with tempfile.NamedTemporaryFile(
                delete=False
            ) as tmp:

                tmp.write(uploaded_file.read())
                temp_path = tmp.name

            extension = uploaded_file.name.split(".")[-1].lower()

            with st.spinner("📂 Preparing File..."):

                if extension in ["mp4", "mov"]:

                    audio_path = extract_audio(
                        temp_path
                    )

                else:

                    audio_path = temp_path

            with st.spinner(
                "🎤 Converting Speech To Text..."
            ):

                transcript, source_lang = transcribe_audio(
                    audio_path,
                    source_lang_ui
                )

            st.success(
                f"Detected Language: {source_lang}"
            )

            with st.spinner(
                "🌍 Translating Content..."
            ):

                translated_text = translate_text(
                    transcript,
                    source_lang,
                    target_lang
                )

            lang_map = {
                "English": "en",
                "Hindi": "hi",
                "Marathi": "mr"
            }

            with st.spinner(
                "🔊 Generating Voice..."
            ):

                audio_file = generate_speech(
                    translated_text,
                    lang_map[target_lang]
                )

            with st.spinner(
                "📜 Creating Subtitles..."
            ):

                srt_file = generate_srt(
                    translated_text
                )

            st.markdown("---")

            result_col1, result_col2 = st.columns(2)

            with result_col1:

                st.subheader(
                    "📝 Transcript"
                )

                st.text_area(
                    "",
                    transcript,
                    height=300
                )

            with result_col2:

                st.subheader(
                    "🌐 Translation"
                )

                st.text_area(
                    "",
                    translated_text,
                    height=300
                )

            st.subheader(
                "🔊 Voice Output"
            )

            st.audio(audio_file)

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

                if os.path.exists(temp_path):

                    os.remove(temp_path)

            except:
                pass