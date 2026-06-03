from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL = "facebook/nllb-200-1.3B"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)

LANG_CODES = {
    "Hindi": "hin_Deva",
    "English": "eng_Latn",
    "Marathi": "mar_Deva"
}

def translate_text(text, source_lang, target_lang):

    if source_lang == target_lang:
        return text

    tokenizer.src_lang = LANG_CODES[source_lang]

    encoded = tokenizer(
        text,
        return_tensors="pt"
    )

    generated_tokens = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(
            LANG_CODES[target_lang]
        ),
        max_length=256
    )

    translated = tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True
    )[0]

    return translated