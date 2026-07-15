# AI Multilingual Grammar Assistant

AI-powered grammar correction web application for English, Hindi, Hinglish, and mixed-language text. The application preserves the original language and writing script while correcting grammar, spelling, punctuation, and capitalization.

Built using **Next.js**, **FastAPI**, **LangChain**, **Ollama**, and **Pydantic**.

---

## Features

- Grammar correction for English, Hindi, Hinglish, and mixed-language text
- Preserves the original language and writing script
- Corrects grammar, spelling, punctuation, and capitalization
- Structured AI responses using Pydantic models
- FastAPI REST API backend
- Responsive Next.js frontend with Tailwind CSS
- Displays detected language
- Displays detailed grammar corrections with explanations
- Loading state for improved user experience

---

## Technology Stack

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

### Backend

- FastAPI
- LangChain
- Ollama
- Pydantic

### AI Model

-  qwen3:1.7b
---
## Design Decisions

- FastAPI was used to expose a lightweight REST API for the frontend.
- LangChain was used to orchestrate prompt execution and structured outputs.
- Pydantic models were used to validate all AI responses before returning them to the client.
- Ollama was chosen to enable local inference without relying on external APIs during development.
- The frontend was built with Next.js and TypeScript to create a modular, component-based interface.

## Project Structure

```text
grammar-assistant/
│
├── backend/
│   ├── app.py
│   ├── chains.py
│   ├── grammar_service.py
│   ├── prompts.py
│   ├── models.py
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## Architecture

```text
                 +----------------------+
                 |      Next.js UI      |
                 +----------+-----------+
                            |
                     HTTP POST /correct
                            |
                            v
                 +----------------------+
                 |     FastAPI API      |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |   LangChain Pipeline |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |   Ollama (qwen3:1.7b) |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 | Structured Response  |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |      Frontend UI     |
                 +----------------------+
```

---

## How It Works

1. The user enters a sentence in the web interface.
2. The frontend sends a POST request to the FastAPI backend.
3. FastAPI invokes a LangChain pipeline.
4. LangChain sends the prompt and user input to the local qwen3:1.7b model via Ollama.
5. The model returns a structured response.
6. Pydantic validates the response.
7. The frontend displays the corrected sentence and grammar corrections.

---

## API

### POST `/correct`

Request

```json
{
  "text": "im happy"
}
```

Response

```json
{
  "language": "English",
  "corrected_text": "I'm happy.",
  "has_errors": true,
  "mistakes": [
    {
      "original": "im",
      "replacement": "I'm",
      "category": "Grammar",
      "reason": "Missing apostrophe."
    }
  ]
}
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/grammar-assistant.git
```

---

### Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app:app --reload
```

The backend runs on:

```
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

The frontend runs on:

```
http://localhost:3000
```

---

## Screenshots

### Home Page
### Grammar Correction

<img width="898" height="690" alt="Screenshot 2026-07-15 at 10 42 25" src="https://github.com/user-attachments/assets/a21d5e8d-b3da-46de-ad7f-354f0c4017fd" />
<img width="890" height="645" alt="Screenshot 2026-07-15 at 10 43 28" src="https://github.com/user-attachments/assets/2ff0483d-e972-404a-a1b2-0b40bc2e0098" />




---

## Future Improvements

- Deploy frontend on Vercel
- Deploy backend on Render
- Replace the local model with a hosted LLM API
- Improve Hinglish correction accuracy
- Add copy-to-clipboard functionality
- Add correction history
- Add grammar quality score
- Support document-level grammar correction

---

## Limitations

This project uses **Qwen3:1.7B** running locally through **Ollama**. While it provides a lightweight, privacy-friendly, and completely offline solution, it has a few limitations:

- **Limited reasoning capability:** As a 1.7B parameter model, it may struggle with complex grammar, ambiguous sentences, and context-heavy inputs.
- **Hinglish variability:** Informal Romanized Hindi (e.g., *kr*, *rha*, *h*, *gya*) may not always be normalized correctly due to the lack of standardized spelling.
- **Punctuation inconsistencies:** The model may occasionally miss commas, question marks, or full stops in corrected sentences.
- **Prompt sensitivity:** Smaller language models are highly sensitive to prompt design. Longer or more complex prompts can result in inconsistent or empty responses.
- **Structured output reliability:** Unlike larger commercial models, Qwen3:1.7B may occasionally return malformed or incomplete JSON, requiring additional validation and error handling in the backend.
- **Context limitations:** The model only processes the current input and cannot infer missing information or resolve ambiguous sentences with high confidence.
- **Performance:** Running locally on consumer hardware may result in slower response times compared to cloud-hosted LLMs.
- **No external knowledge:** The model operates without internet access and cannot verify facts or retrieve real-time information.

### Future Improvements

- Upgrade to a larger multilingual model (e.g., Qwen3:4B or Gemma 3 4B) for improved grammar correction accuracy.
- Integrate cloud-based models such as Gemini or GPT for higher-quality multilingual corrections.
- Improve Hinglish normalization by expanding prompt examples or fine-tuning on Romanized Hindi datasets.
- Enhance punctuation restoration and contextual grammar correction.
- Add confidence scoring and fallback mechanisms for uncertain corrections.
- Support streaming responses for a smoother user experience.
---

## Learning Outcomes

This project provided hands-on experience with:

- React and Next.js
- TypeScript
- Tailwind CSS
- FastAPI
- REST API development
- LangChain
- Prompt engineering
- Ollama
- Structured LLM outputs
- Pydantic
- Full-stack AI application development

---
