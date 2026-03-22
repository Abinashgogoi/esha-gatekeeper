import re


def normalize_text(text: str) -> str:
    if not text:
        return ""

    text = text.strip().lower()

    # collapse repeated spaces
    text = re.sub(r"\s+", " ", text)

    # light vowel normalization
    text = text.replace("aa", "a")
    text = text.replace("ee", "e")
    text = text.replace("oo", "o")
    text = text.replace("uu", "u")

    return text
