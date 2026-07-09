type ResultCardProps = {
  language: string;
  correctedText: string;
};

export default function ResultCard({
  language,
  correctedText,
}: ResultCardProps) {
  return (
    <div className="border rounded-lg mt-8 p-6">

      <h2 className="font-bold">
        Language
      </h2>

      <p>{language}</p>

      <h2 className="font-bold mt-4">
        Corrected Text
      </h2>

      <p>{correctedText}</p>

    </div>
  );
}
