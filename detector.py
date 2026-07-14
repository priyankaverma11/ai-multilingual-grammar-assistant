#language detector- english/hindi/hinglish
import re

HINGLISH_WORDS = {
    "mai",
    "main",
    "mera",
    "meri",
    "mere",
    "tum",
    "tera",
    "teri",
    "hai",
    "tha",
    "thi",
    "the",
    "nahi",
    "nhi",
    "kya",
    "kaise",
    "kyu",
    "gya",
    "gayi",
    "raha",
    "rahi",
    "hu",
    "hun",
    "haan"
}


def detect_language(text: str) -> str:

    # Rule 1: Hindi (Devanagari Unicode)
    if re.search(r'[\u0900-\u097F]', text):
        return "Hindi"

    # Rule 2: Hinglish
    words = text.lower().split()

    for word in words:
        if word in HINGLISH_WORDS:
            return "Hinglish"

    # Rule 3: Default
    return "English"