type GrammarFormProps = {
  sentence: string;
  setSentence: (value: string) => void;
  onCorrect: () => void;
  loading: boolean;
};

export default function GrammarForm({
  sentence,
  setSentence,
  onCorrect,
  loading
}: GrammarFormProps) {
  return (
    <>
      <textarea
        value={sentence}
        onChange={(e) => setSentence(e.target.value)}
        placeholder="Type your sentence here..."
        className="mt-6 w-full h-40 p-4 rounded-xl border border-zinc-700 bg-zinc-950 placeholder:text-zinc-500"
      />

      <button
        onClick={onCorrect}
         disabled={loading || sentence.trim() === ""}
    
        className="
        mt-6
        bg-blue-600
        hover:bg-blue-700
        transition-all
        duration-200
        cursor-pointer
        text-white
        px-6
        py-3
        rounded-xl"
      >
        {loading ? "Correcting..." : "Correct Grammar"}
      </button>
    </>
  );
}