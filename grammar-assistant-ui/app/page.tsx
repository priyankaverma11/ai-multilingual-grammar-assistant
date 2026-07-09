"use client";
import GrammarForm from "@/components/GrammarForm";

import { useState } from "react";

export default function Home() {
  const [sentence, setSentence] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const handleCorrect = async () => {
  setLoading(true);

  try {
    const response = await fetch("http://127.0.0.1:8000/correct", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: sentence,
      }),
    });

    const data = await response.json();
    setResult(data);
  } finally {
    setLoading(false);
  }
};

  return (
    <main className="min-h-screen flex justify-center items-center" >
      <div className="w-full max-w-2xl bg-zinc-900 rounded-2xl p-8 shadow-2xl"> 
      
       <h1 className="text-4xl font-bold">
        Grammar Assistant
       </h1>

      <p className="mt-4 text-gray-400">
        Correct grammar in English, Hindi and Hinglish.
      </p>

      

      <GrammarForm
       sentence={sentence}
       setSentence={setSentence}
       onCorrect={handleCorrect}
       loading={loading}
      />

      <p className="mt-4 text-green-400">
        {result?.corrected_text }
      </p>
      
      </div>


    </main>
  );
}