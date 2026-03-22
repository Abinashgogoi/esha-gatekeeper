INTENT_PATTERNS = {
    "translate": [
        (r"\btranslate\b", 3),
        (r"\btranslation\b", 3),
        (r"\bonubad\b", 3),
        (r"\banuvad\b", 3),
        (r"\bto english\b", 3),
        (r"\bin english\b", 2),
        (r"\bto assamese\b", 3),
        (r"\bin assamese\b", 2),
        (r"\benglish\b", 1),
        (r"\bassamese\b", 1),
    ],
    "weather": [
        (r"\bweather\b", 3),
        (r"\bmausam\b", 3),
        (r"\btemperature\b", 3),
        (r"\bclimate\b", 2),
        (r"\brain\b", 2),
    ],
    "memory": [
        (r"\bremember\b", 3),
        (r"\byaad\b", 3),
        (r"\bmonot\b", 3),
        (r"\bsave\b", 2),
        (r"\bstore\b", 2),
        (r"\bnote this\b", 3),
    ],
}
