from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

MODEL = "facebook/nllb-200-1.3B"

tokenizer = None
model = None

LANG_CODES = {
    "English": "eng_Latn",
    "Hindi": "hin_Deva",
    "Marathi": "mar_Deva",
    "Gujarati": "guj_Gujr",
    "Punjabi": "pan_Guru",
    "Bengali": "ben_Beng",
    "Odia": "ory_Orya",
    "Kannada": "kan_Knda",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Malayalam": "mal_Mlym",
    "Urdu": "urd_Arab"
}


def load_model():

    global tokenizer
    global model

    if tokenizer is None:

        print("Loading NLLB Tokenizer...")

        tokenizer = AutoTokenizer.from_pretrained(
            MODEL
        )

    if model is None:

        print("Loading NLLB Model...")

        model = AutoModelForSeq2SeqLM.from_pretrained(
            MODEL
        )

        print("NLLB Ready")

    return tokenizer, model


def translate_once(
    text,
    source_lang,
    target_lang
):

    if not text.strip():
        return ""

    tokenizer, model = load_model()

    print(
        f"TRANSLATING: "
        f"{source_lang} -> {target_lang}"
    )

    tokenizer.src_lang = (
        LANG_CODES[source_lang]
    )

    encoded = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    max_length=512
    )

    generated_tokens = model.generate(
        **encoded,
        forced_bos_token_id=
        tokenizer.convert_tokens_to_ids(
            LANG_CODES[target_lang]
        ),
        max_length=512,
        num_beams=4,
        length_penalty=1.0,
        do_sample=False,
        early_stopping=True
    )

    translated = tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True
    )[0]

    return translated.strip()


def translate_segment(
    text,
    source_lang,
    target_lang
):

    return translate_once(
        text,
        source_lang,
        target_lang
    )


def translate_text(
    text,
    source_lang,
    target_lang
):

    if source_lang == target_lang:
        return text

    indian_langs = {
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
    }

    if (
        source_lang in indian_langs
        and target_lang in indian_langs
        and source_lang != "Hindi"
        and target_lang != "Hindi"
    ):

        print(
            f"Using Hindi Pivot: "
            f"{source_lang} -> Hindi -> "
            f"{target_lang}"
        )

        hindi_text = translate_once(
            text,
            source_lang,
            "Hindi"
        )

        return translate_once(
            hindi_text,
            "Hindi",
            target_lang
        )

    return translate_once(
        text,
        source_lang,
        target_lang
    )