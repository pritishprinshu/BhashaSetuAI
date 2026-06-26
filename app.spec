# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import (
    collect_submodules,
    collect_data_files,
    copy_metadata
)

# Hidden imports
hiddenimports = (
    collect_submodules("transformers")
    + collect_submodules("faster_whisper")
    + collect_submodules("TTS")
)

# Data files
datas = [
    ("backend", "backend"),
    ("models", "models"),
    ("samples", "samples"),
    ("ui.py", "."),
]

# XTTS / TTS package resources
datas += collect_data_files("TTS")

# Streamlit metadata
datas += copy_metadata("streamlit")

# XTTS metadata
datas += copy_metadata("TTS")

# Transformers metadata
datas += copy_metadata("transformers")

# Other metadata
try:
    datas += copy_metadata("altair")
except:
    pass

try:
    datas += copy_metadata("pyarrow")
except:
    pass

try:
    datas += copy_metadata("faster-whisper")
except:
    pass

a = Analysis(
    ["app.py"],
    pathex=[],
    binaries=[],
    datas=datas,

    hiddenimports=hiddenimports + [
        "streamlit",
        "transformers",
        "faster_whisper",
        "piper",
        "ffmpeg",
        "soundfile",
        "sentencepiece",
        "accelerate",
        "torch",
        "torchaudio",
        "TTS",
    ],

    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="BhashaSetuAI",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="BhashaSetuAI",
)