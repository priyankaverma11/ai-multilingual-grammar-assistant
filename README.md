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

- Llama 3.2 (3B)

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
                 |   Ollama (Llama 3.2) |
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
4. LangChain sends the prompt and user input to the local Llama 3.2 model via Ollama.
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

_Add screenshot_

### Grammar Correction

_Add screenshot_

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

- Hinglish written in Roman script is inherently ambiguous and may produce inconsistent corrections depending on the underlying language model.
- The current implementation uses a locally hosted Llama 3.2 model through Ollama. Accuracy and response time depend on the capabilities of the selected model.

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
