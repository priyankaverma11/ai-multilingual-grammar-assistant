import re
from models import GrammarResponse
from chains import grammar_chain
from language_detector import detect_language

def correct_text(text: str) -> GrammarResponse:

    text = text.strip()

    if not text:
        return GrammarResponse(
            language="Unknown",
            corrected_text="",
            has_errors=False,
            mistakes=[]
        )

    # Reject inputs with no letters (English or Hindi)
    if not re.search(r"[A-Za-z\u0900-\u097F]", text):
        return GrammarResponse(
            language="Unknown",
            corrected_text=text,
            has_errors=False,
            mistakes=[]
        )

    language = detect_language(text)

    response = grammar_chain.invoke({
        "text": text
    })

    response.language = language
    response.has_errors = (
        response.corrected_text.strip() != text.strip()
    )

    if not response.has_errors:
        response.mistakes = []

    return response