type TextInputProps = {
  sentence: string;
  setSentence: (value: string) => void;
};

export default function TextInput({
  sentence,
  setSentence,
}: TextInputProps) {
  return (
    <textarea
      className="border rounded-lg w-full h-40 p-4"
      placeholder="Enter a sentence..."
      value={sentence}
      onChange={(e) => setSentence(e.target.value)}
    />
  );
}
