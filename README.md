# 🌍 BhashaSetuAI Documentation Suite

## Version

**v1.0.0-beta**

---

# 📖 Table of Contents

1. Project Overview
2. Features
3. System Architecture
4. Project Structure
5. Technology Stack
6. Installation Guide
7. Windows Installation
8. macOS Installation
9. Linux Installation
10. Running the Application
11. Building Windows Executable
12. Creating Windows Installer
13. Model Management
14. Repository Structure
15. Git Workflow
16. Hardware Requirements
17. Troubleshooting
18. Deployment Guide
19. Future Roadmap
20. License

---

# 1. Project Overview

## What is BhashaSetuAI?

BhashaSetuAI is an **offline multilingual audio and video translation platform** designed to translate spoken content between Indian languages while preserving user privacy.

The system performs:

* Speech-to-Text (Whisper)
* Language Detection
* Translation (NLLB)
* Text-to-Speech (XTTS / Piper)
* Audio & Video Generation

No internet connection is required after models are installed.

---

# 2. Features

✅ Offline Translation

✅ Automatic Language Detection

✅ Whisper Speech Recognition

✅ NLLB Translation

✅ XTTS Voice Synthesis

✅ Piper TTS Support

✅ Audio Translation

✅ Video Translation

✅ Subtitle Generation

✅ Streamlit Dashboard

---

# 3. System Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Upload Audio/Video
 │
 ▼
FFmpeg Audio Extraction
 │
 ▼
Whisper STT
 │
 ▼
Language Detection
 │
 ▼
NLLB Translation
 │
 ▼
XTTS / Piper
 │
 ▼
FFmpeg Merge
 │
 ▼
Translated Audio / Video
```

---

# 4. Project Structure

```text
BhashaSetuAI/

├── app.py
├── launch.py
├── backend/
│   ├── stt.py
│   ├── translator.py
│   ├── xtts.py
│   ├── tts.py
│   ├── video.py
│   ├── video_translate.py
│   ├── speaker.py
│   └── subtitles.py
│
├── models/
│   ├── voices/
│   ├── README.md
│   └── download_models.py
│
├── assets/
├── docs/
├── scripts/
├── tests/
├── samples/
├── outputs/
├── uploads/
└── requirements.txt
```

---

# 5. Technology Stack

| Component            | Technology      |
| -------------------- | --------------- |
| Frontend             | Streamlit       |
| STT                  | Faster-Whisper  |
| Translation          | Meta NLLB-200   |
| TTS                  | XTTS v2 / Piper |
| Video Processing     | FFmpeg          |
| Programming Language | Python 3.11     |

---

# 6. Installation Guide

## Windows

1. Install Python 3.11
2. Install Git
3. Install FFmpeg
4. Clone or extract the project
5. Create a virtual environment
6. Install requirements
7. Run Streamlit

## macOS

```bash
brew install python@3.11
brew install ffmpeg

python3.11 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

## Linux

```bash
sudo apt install python3.11 python3.11-venv ffmpeg

python3.11 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

---

# 7. Running the Application

Windows

```cmd
venv\Scripts\activate

streamlit run app.py
```

macOS / Linux

```bash
source venv/bin/activate

streamlit run app.py
```

---

# 8. Windows Executable

Build using:

```cmd
pyinstaller app.spec
```

Output:

```
dist/
    BhashaSetuAI.exe
```

---

# 9. Windows Installer

Recommended:

* PyInstaller
* Inno Setup

Output:

```
BhashaSetuAI_Setup.exe
```

Installation Experience:

```
Next
↓

Next
↓

Install
↓

Finish
```

---

# 10. Model Management

Large AI models should **not** be committed to Git.

Instead:

```
models/

download_models.py

voices/
```

On first run:

* Check model availability
* Download if missing
* Store locally
* Run completely offline afterwards

---

# 11. Git Workflow

```
main

↓

development

↓

feature/*
```

Never develop directly on `main`.

---

# 12. Hardware Requirements

Minimum

* CPU: Intel i5 / Ryzen 5
* RAM: 8 GB
* Storage: 15 GB
* Python: 3.11

Recommended

* CPU: Intel i7 / Ryzen 7
* RAM: 16 GB+
* GPU: NVIDIA RTX 3060 (or better) for faster processing
* SSD Storage

---

# 13. Repository Cleanup

Never commit:

```
venv/
xtts_env/
outputs/
uploads/
build/
dist/
release/
*.zip
__pycache__/
```

---

# 14. Troubleshooting

## FFmpeg Not Found

Install FFmpeg and ensure it is available in the system PATH.

## Torch Installation Issues

Use Python 3.11 and reinstall with the correct package versions.

## Slow Processing

* Use a GPU if available.
* Prefer Faster-Whisper over standard Whisper.
* Keep models on an SSD.

---

# 15. Deployment

Developer

```
Git Clone

↓

Install Requirements

↓

Run
```

End User

```
Download Installer

↓

Install

↓

Launch Application
```

---

# 16. Future Roadmap

* GPU acceleration
* Speaker diarization
* Subtitle editor
* Docker deployment
* Automatic model downloader
* Windows installer
* macOS application bundle
* Linux package
* Real-time streaming translation

---

# 17. License

MIT License

---

# 18. Author

**Pritish Prinshu**

BhashaSetuAI — Offline Multilingual Audio & Video Translation Platform

2026
