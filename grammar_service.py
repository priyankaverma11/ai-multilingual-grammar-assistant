import re
import json

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
    print(response.content)

    print("========== RAW CONTENT ==========")
    print(repr(response.content))
    print("=================================")
    print("RAW CONTENT:", repr(response.content))
    try: 
        data = json.loads(response.content)
    except Exception as e:
        print("JSON ERROR:", e)
        return GrammarResponse(
            language=language,
            corrected_text=response.content,
            has_errors=False,
            mistakes=[]
        )

    corrected = data.get("corrected_text", text)

    return GrammarResponse(
        language=language,
        corrected_text=corrected,
        has_errors=(corrected.strip() != text.strip()),
        mistakes=[]
    )

    #corrected = data.get("corrected_text", text)

    #return GrammarResponse(
      #  language=language,
       # corrected_text=corrected,
        #has_errors=(corrected.strip() != text.strip()),
        #mistakes=[]
   # )