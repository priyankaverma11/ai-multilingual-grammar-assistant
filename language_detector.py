import re

ROMAN_HINDI_WORDS = {
    "hai", "ho", "hu", "hoon",
    "mai", "main", "mera", "meri",
    "tum", "kya", "ka", "ki", "ke",
    "gaya", "gya", "tha", "thi",
    "haan", "nahi", "kyu", "kahan"
}

ENGLISH_WORDS = {
    "the", "is", "are", "and", "you",
    "happy", "school", "office",
    "going", "went", "good", "today"
}


def detect_language(text: str) -> str:
    text = text.strip()

    # Hindi (Devanagari)
    if re.search(r'[\u0900-\u097F]', text):
        return "Hindi"

    words = re.findall(r"[A-Za-z']+", text.lower())

    hindi_count = sum(word in ROMAN_HINDI_WORDS for word in words)
    english_count = sum(word in ENGLISH_WORDS for word in words)

    if hindi_count > 0 and english_count > 0:
        return "Mixed"

    if hindi_count > 0:
        return "Hinglish"

    return "English"