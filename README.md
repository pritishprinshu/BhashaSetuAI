# 🌍 BhashaSetuAI

> **Offline Multilingual Audio & Video Translation Platform for Indian Languages**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Whisper](https://img.shields.io/badge/OpenAI-Whisper-green)
![NLLB](https://img.shields.io/badge/Meta-NLLB-orange)
![XTTS](https://img.shields.io/badge/Coqui-XTTS-purple)
![Offline](https://img.shields.io/badge/Mode-Offline-success)

</p>

---

## 📌 Overview

BhashaSetuAI is an **offline multilingual Audio & Video Translation Platform** designed to break language barriers in **education, healthcare, agriculture, and government services**.

The system automatically:

* 🎤 Converts speech to text
* 🌐 Detects the spoken language
* 🔄 Translates content into another Indian language
* 🔊 Generates natural translated speech
* 🎬 Produces a translated audio or video

No internet connection is required after model setup.

---

# ✨ Features

* 🎤 Offline Speech Recognition (Whisper)
* 🌐 Automatic Language Detection
* 🔄 Translation using Meta NLLB-200
* 🔊 Natural Voice Generation (XTTS v2)
* 🎵 Piper TTS Support
* 🎬 Audio & Video Translation
* 📜 Subtitle Generation
* ⚡ Live Translation Preview
* 🔒 Privacy First (Offline Processing)

---

# 🏗 System Architecture

```text
                User
                  │
                  ▼
          Streamlit Web UI
                  │
                  ▼
        Upload Audio / Video
                  │
                  ▼
     FFmpeg Audio Extraction
                  │
                  ▼
       Whisper Speech-to-Text
                  │
                  ▼
      Language Detection
                  │
                  ▼
        NLLB Translation
                  │
                  ▼
        XTTS / Piper TTS
                  │
                  ▼
      FFmpeg Video Rendering
                  │
                  ▼
      Download Translated Output
```

---

# 🌍 Supported Languages

* English
* Hindi
* Marathi
* Gujarati
* Punjabi
* Bengali
* Tamil
* Telugu
* Kannada
* Malayalam
* Odia
* Urdu

---

# 💻 Tech Stack

| Component            | Technology      |
| -------------------- | --------------- |
| Frontend             | Streamlit       |
| STT                  | Whisper         |
| Translation          | NLLB-200        |
| TTS                  | XTTS v2 / Piper |
| Video Processing     | FFmpeg          |
| Programming Language | Python          |

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/BhashaSetuAI.git
cd BhashaSetuAI
```

Create a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 📂 Project Structure

```text
BhashaSetuAI/
│
├── app.py
├── backend/
├── models/
├── assets/
├── docs/
├── scripts/
├── uploads/
├── outputs/
└── requirements.txt
```

---

# 🔒 Privacy

All processing happens locally on the user's machine.

No audio, video, or transcript is uploaded to external servers.

---

# 🛣 Roadmap

* [ ] GPU Acceleration
* [ ] Speaker Diarization
* [ ] Real-Time Translation
* [ ] Subtitle Editing
* [ ] Docker Deployment
* [ ] Windows Installer
* [ ] Executable (.exe)
* [ ] Mobile Version

---

# 👨‍💻 Author

**Pritish Prinshu**

AI Engineer | Multilingual AI | Offline Translation Systems

---

# 📄 License

This project is licensed under the MIT License.
